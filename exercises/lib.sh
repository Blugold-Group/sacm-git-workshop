# Shared helpers for the exercise scripts. Sourced, not run directly.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLAYGROUND="$REPO_ROOT/playground"

# Create a fresh, empty sandbox repo at playground/<name> and cd into it.
# playground/ is in .gitignore, so nothing here touches the workshop repo.
new_sandbox() {
  local dir="$PLAYGROUND/$1"
  if [ -e "$dir" ]; then
    echo "Removing the old $1 sandbox..."
    rm -rf -- "$dir"
  fi
  mkdir -p "$dir"
  cd "$dir"
  git init --quiet --initial-branch=main
  # Use a placeholder identity only if you haven't set one yet.
  git config user.name >/dev/null || git config user.name "Workshop Student"
  git config user.email >/dev/null || git config user.email "student@example.com"
}

commit() {
  git add -A
  git commit --quiet -m "$1"
}

done_message() {
  echo
  echo "Sandbox ready: $(pwd)"
  echo "Next:  cd \"$(pwd)\""
}
