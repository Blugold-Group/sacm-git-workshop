#!/usr/bin/env bash
# Builds a sandbox repo with a few mistakes to undo.
source "$(dirname "$0")/../lib.sh"

new_sandbox undo

cat > grades.py <<'EOF'
def average(scores):
    return sum(scores) / len(scores)
EOF
commit "Add average function"

cat > README.md <<'EOF'
# Grade Calculator
EOF
commit "Add readme"

# Mistake: a commit that breaks the code.
cat > grades.py <<'EOF'
def average(scores):
    return sum(scores) / 0
EOF
commit "Optimize average"

# Mistake: a typo in the latest commit message.
cat >> README.md <<'EOF'

Computes the average of a list of scores.
EOF
commit "Updaet readme"

# Mistake: an unwanted edit that isn't committed.
echo "print('debugging!!!')" >> grades.py

# Mistake: a secrets file staged by accident.
echo "API_KEY=not-a-real-key" > .env
git add .env

done_message
echo "Then:  git status"
