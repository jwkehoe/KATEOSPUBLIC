#!/usr/bin/env python3
"""Local subscription allowance ledger. No credentials, billing API, or daemon."""
import argparse
import datetime as dt
import fcntl
import json
import math
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'LOCAL/usage-burn/ledger.jsonl'


def timestamp(value):
    parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('timestamp must include timezone')
    return parsed.timestamp()


def number(value, low=0, high=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError('expected a finite number')
    if value < low or (high is not None and value > high):
        raise ValueError('number outside allowed range')
    return value


def normalize(payload, meta):
    """Whitelist counters only; discard account identifiers and raw tool data."""
    timestamp(meta['observed_at'])
    buckets = payload.get('rateLimitsByLimitId')
    if not buckets:
        legacy = payload.get('rateLimits')
        buckets = {legacy.get('limitId', 'codex'): legacy} if legacy else {}
    windows = []
    for bucket, limits in buckets.items():
        if not limits:
            continue
        for name in ('primary', 'secondary'):
            window = limits.get(name)
            if not window or window.get('usedPercent') is None:
                continue
            windows.append(dict(bucket=bucket, name=name, unit='percent',
                                used=number(window['usedPercent'], high=100), capacity=100,
                                resets_at=number(window['resetsAt']),
                                duration_minutes=number(window['windowDurationMins'], low=1)))
    # Manual Chat/UI counters use a separate pool and may use message counts.
    for window in payload.get('windows', []):
        capacity = number(window['capacity'], low=1)
        windows.append(dict(bucket=str(window['bucket']), name=str(window['name']),
                            unit=window['unit'], used=number(window['used'], high=capacity),
                            capacity=capacity, resets_at=number(window['resets_at']),
                            duration_minutes=number(window['duration_minutes'], low=1)))
    if not windows:
        raise ValueError('no supplied measurable windows; unavailable is not zero')
    keys = [(w['bucket'], w['name']) for w in windows]
    if len(keys) != len(set(keys)):
        raise ValueError('duplicate window')
    return dict(schema_version=1, id=str(uuid.uuid4()), **meta, windows=windows)


def append(path, record):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+', encoding='utf-8') as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        stream.seek(0)
        prior = [json.loads(line) for line in stream if line.strip()]
        if any(r['pool'] == record['pool'] and timestamp(r['observed_at']) > timestamp(record['observed_at']) for r in prior):
            raise ValueError('out-of-order snapshot in pool')
        stream.seek(0, 2)
        stream.write(json.dumps(record, sort_keys=True) + '\n')
        stream.flush()
    return record


def review(records, pool, now, reserve=10, planned_hours=None):
    items = sorted((r for r in records if r['pool'] == pool), key=lambda r: timestamp(r['observed_at']))
    if not items:
        return dict(pool=pool, status='no observations', windows=[])
    latest = items[-1]
    result = dict(pool=pool, as_of=latest['observed_at'], observation_age_minutes=(now-timestamp(latest['observed_at']))/60,
                  attribution='account-wide; project/model labels do not prove causation', windows=[])
    for current in latest['windows']:
        remaining = current['capacity'] - current['used']
        reset_hours = (current['resets_at'] - now)/3600
        row = dict(**current, remaining=remaining, hours_to_reset=max(0, reset_hours),
                   status='expired snapshot' if reset_hours <= 0 else 'baseline only')
        intervals = []
        for before, after in zip(items, items[1:]):
            key = (current['bucket'], current['name'])
            a = next((w for w in before['windows'] if (w['bucket'], w['name']) == key), None)
            b = next((w for w in after['windows'] if (w['bucket'], w['name']) == key), None)
            if not a or not b:
                continue
            hours = (timestamp(after['observed_at'])-timestamp(before['observed_at']))/3600
            same = all(a[k] == b[k] == current[k] for k in ('resets_at', 'capacity', 'unit', 'duration_minutes'))
            if not same or hours <= 0 or b['used'] < a['used'] or timestamp(after['observed_at']) >= b['resets_at']:
                continue
            delta = b['used']-a['used']
            intervals.append(dict(hours=hours, burn=delta, rate=delta/hours,
                                  project=after['project'], model=after['model'],
                                  concurrent=after['concurrent'], completed_units=after['completed_units'],
                                  outcome=after['outcome']))
        row['intervals'] = intervals
        if intervals and reset_hours > 0:
            recent = intervals[-1]
            rate = recent['rate']
            row.update(status='measured interval; conditional projection' if rate else 'no visible burn; resolution limited',
                       recent_burn=recent['burn'], rate_per_hour=rate,
                       weighted_rate_per_hour=sum(i['burn'] for i in intervals)/sum(i['hours'] for i in intervals),
                       reserve_units=current['capacity']*reserve/100)
            usable = max(0, remaining-row['reserve_units'])
            row['hours_to_reserve'] = usable/rate if rate else None
            row['depletes_before_reset'] = remaining/rate < reset_hours if rate else None
            if recent['completed_units']:
                row['burn_per_completed_unit'] = recent['burn']/recent['completed_units']
            if planned_hours is not None:
                row['projected_burn'] = rate*planned_hours
                row['fits_with_reserve'] = rate*planned_hours <= usable
                row['crosses_reset'] = planned_hours > reset_hours
        result['windows'].append(row)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ledger', type=Path, default=DEFAULT)
    sub = parser.add_subparsers(dest='command', required=True)
    capture = sub.add_parser('capture')
    capture.add_argument('--pool', required=True, help='e.g. codex-work or chat-model-name; never combine unrelated limits')
    capture.add_argument('--project', required=True)
    capture.add_argument('--source', required=True)
    capture.add_argument('--observed-at', default=dt.datetime.now(dt.timezone.utc).isoformat())
    capture.add_argument('--model', default='unknown')
    capture.add_argument('--effort', default='unknown')
    capture.add_argument('--speed', default='unknown')
    capture.add_argument('--concurrent', choices=['unknown', 'yes', 'no'], default='unknown')
    capture.add_argument('--completed-units', type=float, default=0)
    capture.add_argument('--outcome', choices=['baseline', 'progress', 'completed', 'failed'], default='baseline')
    capture.add_argument('--input', type=Path, help='normalized or tool JSON; defaults to stdin')
    report = sub.add_parser('review')
    report.add_argument('--pool', required=True)
    report.add_argument('--reserve-percent', type=float, default=10)
    report.add_argument('--planned-hours', type=float)
    args = parser.parse_args()
    try:
        if args.command == 'capture':
            payload = json.loads(args.input.read_text() if args.input else sys.stdin.read())
            meta = {k: getattr(args, k) for k in ('pool','project','source','observed_at','model','effort','speed','concurrent','completed_units','outcome')}
            number(meta['completed_units'])
            output = append(args.ledger, normalize(payload, meta))
        else:
            number(args.reserve_percent, high=100)
            if args.planned_hours is not None:
                number(args.planned_hours)
            records = [json.loads(line) for line in args.ledger.read_text().splitlines() if line.strip()] if args.ledger.exists() else []
            output = review(records, args.pool, dt.datetime.now(dt.timezone.utc).timestamp(), args.reserve_percent, args.planned_hours)
        print(json.dumps(output, indent=2))
    except (ValueError, KeyError, OSError) as error:
        parser.exit(2, f'usage-burn: {error}\n')


if __name__ == '__main__':
    main()
