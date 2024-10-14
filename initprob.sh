#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <ParentDirectoryName> <SubDirectoryName>"
    exit 1
fi

PARENT_DIR="$1"
SUB_DIR="$2"

mkdir -p "$PARENT_DIR/$SUB_DIR"


touch "$PARENT_DIR/$SUB_DIR/solution.py"
touch "$PARENT_DIR/$SUB_DIR/takeaways.md"


echo "Topics in this problem:" >> "$PARENT_DIR/$SUB_DIR/takeaways.md"
echo "" >> "$PARENT_DIR/$SUB_DIR/takeaways.md"
echo "Takeaways & Big ideas: " >> "$PARENT_DIR/$SUB_DIR/takeaways.md"
echo "" >> "$PARENT_DIR/$SUB_DIR/takeaways.md"
echo "Analysis: " >> "$PARENT_DIR/$SUB_DIR/takeaways.md"
echo "" >> "$PARENT_DIR/$SUB_DIR/takeaways.md"

cursor "$PARENT_DIR/$SUB_DIR/solution.py"

echo "Created directory $PARENT_DIR/$SUB_DIR and file solution.py inside it."
