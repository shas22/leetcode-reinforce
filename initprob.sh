#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <ParentDirectoryName> <SubDirectoryName>"
    exit 1
fi

# Assign arguments to variables
PARENT_DIR="$1"
SUB_DIR="$2"

# Create the subdirectory inside the parent directory
mkdir -p "$PARENT_DIR/$SUB_DIR"

# Create the Python file inside the subdirectory
touch "$PARENT_DIR/$SUB_DIR/solution.py"
touch "$PARENT_DIR/$SUB_DIR/takeaways.md"

# Make takeaway with some template inside
# Append lines to the file
echo "Topics in this problem:" >> "$PARENT_DIR/$SUB_DIR/takeaways.md"
echo "" >> "$PARENT_DIR/$SUB_DIR/takeaways.md"
echo "Takeaways & Big ideas: " >> "$PARENT_DIR/$SUB_DIR/takeaways.md"
echo "" >> "$PARENT_DIR/$SUB_DIR/takeaways.md"
echo "Analysis: " >> "$PARENT_DIR/$SUB_DIR/takeaways.md"
echo "" >> "$PARENT_DIR/$SUB_DIR/takeaways.md"

# open file after creation
code "$PARENT_DIR/$SUB_DIR/solution.py"

echo "Created directory $PARENT_DIR/$SUB_DIR and file solution.py inside it."
