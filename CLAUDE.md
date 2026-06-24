# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A structured Python learning project for a JavaScript developer. Uses a "learn by comparison" approach with Chinese comments and output. Files are numbered sequentially (01-05) with increasing complexity.

## Running Code

Each Python file is a standalone script. Run directly:
```bash
python py_basic/01_basics.py
python backend_basic/10_sqlalchemy_basic.py
```

py_basic/ 下的文件只用标准库。backend_basic/ 需要安装依赖：
```bash
pip install fastapi uvicorn sqlalchemy
```

## Project Structure

### py_basic/ — Python 基础
- `01_basics.py` → Variables, types, strings, lists
- `02_conditions_loops.py` → if/elif/else, for loops
- `03_dict_tuple.py` → Dictionaries and tuples
- `04_functions.py` → Functions, default params, *args
- `05_classes.py` → Classes and inheritance
- `06_error_handling.py` → try/except, custom exceptions
- `07_list_comprehension.py` → List/dict comprehension
- `08_file_io.py` → File read/write

### backend_basic/ — 后端开发
- `09_modules.py` → Modules and imports
- `fastapi_basic.py` → FastAPI routes, params, Pydantic

### backend_basic/db_basic/ — 数据库
- `10_sqlalchemy_basic.py` → SQLAlchemy ORM CRUD

### 其他
- `.learn/progress.json` → Learning progress tracking
- `.learn/python/` → 学习笔记 (markdown)

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
