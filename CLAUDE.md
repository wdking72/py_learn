# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A structured Python learning project for a JavaScript developer. Uses a "learn by comparison" approach with Chinese comments and output. Files are numbered sequentially (01-05) with increasing complexity.

## Running Code

Each Python file is a standalone script. Run directly:
```bash
python 01_basics.py
python 05_classes.py
```

No external dependencies — all files use only Python standard library.

## Project Structure

- `01_basics.py` → Variables, types, strings, lists
- `02_conditions_loops.py` → if/elif/else, for loops
- `03_dict_tuple.py` → Dictionaries and tuples
- `04_functions.py` → Functions, default params, *args
- `05_classes.py` → Classes and inheritance (in progress)
- `.learn/progress.json` → Learning progress tracking

## Code Conventions

- Comments and print output in Chinese
- f-strings for string formatting
- Each file is self-contained (no imports between files)
- JavaScript equivalents shown in comments for comparison

## Teaching Approach

When helping with this project:
- Explain Python concepts by comparing to JavaScript equivalents
- Keep examples simple and runnable
- Use Chinese for comments and output when appropriate
- Update `.learn/progress.json` when new concepts are completed
