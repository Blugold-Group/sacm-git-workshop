#!/usr/bin/env bash
# Builds a sandbox repo where two branches changed the same line.
source "$(dirname "$0")/../lib.sh"

new_sandbox merge-conflict

cat > settings.py <<'EOF'
APP_NAME = "SACM Tracker"
THEME = "light"

# Database
DB_PATH = "tracker.db"
BACKUP_EVERY_HOURS = 24

# Limits
MAX_USERS = 50
EOF
commit "Add settings"

git switch --quiet -c feature/dark-mode
sed -i.bak 's/THEME = "light"/THEME = "dark"/' settings.py && rm settings.py.bak
commit "Switch theme to dark"

git switch --quiet main
sed -i.bak 's/THEME = "light"/THEME = "uwec-blue"/' settings.py && rm settings.py.bak
sed -i.bak 's/MAX_USERS = 50/MAX_USERS = 100/' settings.py && rm settings.py.bak
commit "Use school colors and raise user limit"

done_message
echo "Then:  git merge feature/dark-mode"
