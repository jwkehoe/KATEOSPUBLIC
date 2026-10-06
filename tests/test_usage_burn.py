import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('burn', Path(__file__).resolve().parents[1]/'scripts/usage_burn.py')
burn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(burn)


def sample(hour, used, reset=2000000000, pool='codex-work'):
    meta = dict(observed_at=f'2026-10-05T{hour:02d}:00:00+00:00', pool=pool,
                project='test', source='fixture', model='unknown', effort='unknown',
                speed='unknown', concurrent='unknown', completed_units=2, outcome='completed')
    payload = dict(accountId='do-not-store', rateLimits=dict(primary=dict(
        usedPercent=used, resetsAt=reset, windowDurationMins=300)))
    return burn.normalize(payload, meta)


class BurnTests(unittest.TestCase):
    def test_rate_reserve_and_project(self):
        result = burn.review([sample(10,10), sample(12,30)], 'codex-work', burn.timestamp('2026-10-05T12:00:00Z'), planned_hours=2)
        row = result['windows'][0]
        self.assertEqual(row['rate_per_hour'],10)
        self.assertEqual(row['hours_to_reserve'],6)
        self.assertEqual(row['burn_per_completed_unit'],10)
        self.assertEqual(row['projected_burn'],20)
        self.assertTrue(row['fits_with_reserve'])

    def test_reset_and_decrease_not_bridged(self):
        for after in (sample(12,5), sample(12,30,2000000100)):
            row = burn.review([sample(10,10),after], 'codex-work', burn.timestamp(after['observed_at']))['windows'][0]
            self.assertEqual(row['status'],'baseline only')
            self.assertNotIn('rate_per_hour',row)

    def test_zero_baseline_stale_and_pool(self):
        self.assertEqual(burn.review([], 'chat', 0)['status'],'no observations')
        records = [sample(10,10),sample(12,10)]
        row = burn.review(records,'codex-work',burn.timestamp(records[-1]['observed_at']))['windows'][0]
        self.assertIsNone(row['hours_to_reserve'])
        self.assertEqual(burn.review(records,'codex-work',2000000001)['windows'][0]['status'],'expired snapshot')
        self.assertEqual(burn.review(records,'chat',0)['status'],'no observations')

    def test_sanitization_and_validation(self):
        self.assertNotIn('accountId', sample(10,1))
        for bad in (-1,101,float('nan'),True):
            with self.assertRaises(ValueError):
                sample(10,bad)
        with self.assertRaises(ValueError):
            burn.timestamp('2026-10-05T10:00:00')

    def test_append_and_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'ledger.jsonl'
            burn.append(path,sample(12,10))
            with self.assertRaises(ValueError):
                burn.append(path,sample(10,5))
            self.assertEqual(len(path.read_text().splitlines()),1)

    def test_chat_manual_messages(self):
        meta=sample(10,1)
        for key in ('schema_version','id','windows'):
            meta.pop(key)
        meta['pool']='chat-model'
        record=burn.normalize(dict(windows=[dict(bucket='chat-model',name='messages',unit='messages',used=3,capacity=40,resets_at=2000000000,duration_minutes=180)]),meta)
        self.assertEqual(record['windows'][0]['capacity'],40)
        self.assertEqual(record['pool'],'chat-model')


if __name__ == '__main__':
    unittest.main()
