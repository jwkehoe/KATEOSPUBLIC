#!/usr/bin/env bash
set -euo pipefail

readonly BACKUP_ROOT="${KATOS_BACKUP_ROOT:-$HOME/KATOSBACKUP}"

usage() {
  cat <<'USAGE'
Usage:
  kateos_recover_config.sh --list
  kateos_recover_config.sh --original LABEL --target PATH --apply [--replace]
  kateos_recover_config.sh --archive PATH --target PATH --apply [--replace]

The command first extracts an archive to a staging directory. --apply is
required before it writes to TARGET. If TARGET already exists and is nonempty,
--replace moves it into ~/KATOSBACKUP/replaced/ before restoration.
USAGE
}

archive=""
original_label=""
target=""
apply=false
replace=false
list=false
while (($#)); do
  case "$1" in
    --list) list=true; shift ;;
    --archive) archive="${2:-}"; shift 2 ;;
    --original) original_label="${2:-}"; shift 2 ;;
    --target) target="${2:-}"; shift 2 ;;
    --apply) apply=true; shift ;;
    --replace) replace=true; shift ;;
    --help|-h) usage; exit 0 ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; usage >&2; exit 2 ;;
  esac
done

if "$list"; then
  find "$BACKUP_ROOT/original-base" "$BACKUP_ROOT/changes" -type f -name '*.tar.gz' -print 2>/dev/null | sort
  exit 0
fi

if [[ -n "$original_label" ]]; then
  [[ "$original_label" =~ ^[A-Za-z0-9._-]+$ ]] || { printf '%s\n' 'Invalid original label.' >&2; exit 2; }
  archive="$BACKUP_ROOT/original-base/$original_label.tar.gz"
fi
[[ -n "$archive" && -f "$archive" ]] || { printf '%s\n' 'A readable --archive or --original LABEL is required.' >&2; exit 2; }
[[ -n "$target" ]] || { printf '%s\n' '--target is required.' >&2; exit 2; }
"$apply" || { printf '%s\n' 'Dry run only. Add --apply to restore.'; exit 0; }

stage="$(mktemp -d)"
trap 'rm -rf "$stage"' EXIT
tar -xzf "$archive" -C "$stage"
mapfile -t entries < <(find "$stage" -mindepth 1 -maxdepth 1 -print)
(( ${#entries[@]} == 1 )) || { printf '%s\n' 'Archive must contain exactly one top-level item.' >&2; exit 2; }

if [[ -e "$target" || -L "$target" ]]; then
  "$replace" || { printf '%s\n' 'Target exists. Re-run with --replace to preserve and replace it.' >&2; exit 2; }
  stamp="$(date -u '+%Y%m%dT%H%M%SZ')"
  mkdir -p "$BACKUP_ROOT/replaced"
  mv "$target" "$BACKUP_ROOT/replaced/${stamp}-$(basename "$target")"
fi

mkdir -p "$(dirname "$target")"
mv "${entries[0]}" "$target"
printf 'Restored %s to %s\n' "$archive" "$target"
