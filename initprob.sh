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

echo "Created directory $PARENT_DIR/$SUB_DIR and file solution.py inside it."
