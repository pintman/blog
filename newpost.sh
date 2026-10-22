#!/bin/bash
# Legt einen neuen Markdown-Post in content/ an und öffnet ihn in VS Code.
# Aufruf: ./newpost.sh [-p] [-n] "Titel" ["tag1, tag2"]
#   -p  status: published (Default: draft)
#   -n  Datei nicht in VS Code öffnen

set -e
cd "$(dirname "$0")"

STATUS=draft
OPEN=1
while getopts "pn" opt; do
    case $opt in
        p) STATUS=published ;;
        n) OPEN=0 ;;
        *) exit 1 ;;
    esac
done
shift $((OPTIND - 1))

if [ -z "$1" ]; then
    echo "Aufruf: $0 [-p] [-n] \"Titel\" [\"tag1, tag2\"]" >&2
    exit 1
fi

TITLE="$1"
TAGS="$2"
SLUG=$(echo "$TITLE" \
    | sed -e 's/Ä/ae/g; s/Ö/oe/g; s/Ü/ue/g; s/ä/ae/g; s/ö/oe/g; s/ü/ue/g; s/ß/ss/g' \
    | LC_ALL=C tr 'A-Z' 'a-z' \
    | LC_ALL=C sed -e 's/[^a-z0-9]/-/g; s/--*/-/g; s/^-//; s/-$//')
FILE="content/$SLUG.md"

if [ -e "$FILE" ]; then
    echo "Fehler: $FILE existiert bereits." >&2
    exit 1
fi

cat > "$FILE" <<EOF
---
title: $TITLE
date: $(date "+%Y-%m-%d %H:%M")
author: marco.bakera
tags: $TAGS
status: $STATUS
slug: $SLUG
---

EOF

echo "$FILE"
[ "$OPEN" = 1 ] && code "$FILE"
exit 0
