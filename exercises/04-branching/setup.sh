#!/usr/bin/env bash
# Builds a sandbox repo with one commit to branch from.
source "$(dirname "$0")/../lib.sh"

new_sandbox branching

cat > menu.txt <<'EOF'
SACM Pizza Night
================
- Cheese
- Pepperoni
EOF
commit "Add pizza night menu"

done_message
echo "Then:  git switch -c feature/drinks"
