#!/usr/bin/env bash
set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
readonly POLICY_FILE="$REPO_ROOT/config/COPY_BEFORE_FIRST_INSTALL_KEEP_FOREVER.conf"
readonly BACKUP_ROOT="${KATOS_BACKUP_ROOT:-$HOME/KATOSBACKUP}"

usage() {
  cat <<'USAGE'
Usage: kateos_backup_config.sh --source PATH --label NAME [--reason TEXT]

Creates a permanent first copy for NAME, if one does not already exist, and a
timestamped archive for this change. Archives are written under ~/KATOSBACKUP
unless KATOS_BACKUP_ROOT is set.
USAGE
}

source_path=""
label=""
reason="unspecified"
while (($#)); do
  case "$1" in
    --source) source_path="${2:-}"; shift 2 ;;
    --label) label="${2:-}"; shift 2 ;;
    --reason) reason="${2:-}"; shift 2 ;;
    --help|-h) usage; exit 0 ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; usage >&2; exit 2 ;;
  esac
done

[[ -n "$source_path" && -e "$source_path" ]] || { printf '%s\n' 'A readable --source is required.' >&2; exit 2; }
[[ "$label" =~ ^[A-Za-z0-9._-]+$ ]] || { printf '%s\n' 'Label may use letters, numbers, dot, underscore, and hyphen.' >&2; exit 2; }
[[ -f "$POLICY_FILE" ]] || { printf 'Missing policy file: %s\n' "$POLICY_FILE" >&2; exit 2; }

mkdir -p "$BACKUP_ROOT/original-base" "$BACKUP_ROOT/changes" "$BACKUP_ROOT/manifests"
if [[ ! -f "$BACKUP_ROOT/COPY_BEFORE_FIRST_INSTALL_KEEP_FOREVER.conf" ]]; then
  cp "$POLICY_FILE" "$BACKUP_ROOT/COPY_BEFORE_FIRST_INSTALL_KEEP_FOREVER.conf"
fi

source_parent="$(cd "$(dirname "$source_path")" && pwd)"
source_name="$(basename "$source_path")"
timestamp="$(date -u '+%Y%m%dT%H%M%SZ')"

archive() {
  local output="$1"
  tar -C "$source_parent" -czf "$output" "$source_name"
  shasum -a 256 "$output" > "$output.sha256"
}

original="$BACKUP_ROOT/original-base/$label.tar.gz"
if [[ ! -f "$original" ]]; then
  archive "$original"
  printf 'Created permanent original copy: %s\n' "$original"
else
  printf 'Preserved existing permanent original copy: %s\n' "$original"
fi

change_base="$BACKUP_ROOT/changes/${timestamp}-${label}"
change="$change_base.tar.gz"
serial=1
while [[ -e "$change" ]]; do
  printf -v suffix -- '-%02d' "$serial"
  change="$change_base$suffix.tar.gz"
  ((serial += 1))
done
archive "$change"
printf '%s\t%s\t%s\t%s\n' "$timestamp" "$label" "$source_path" "$reason" >> "$BACKUP_ROOT/manifests/changes.tsv"
printf 'Created timestamped copy: %s\n' "$change"
