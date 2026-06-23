# 模块与导入笔记

## 1. 导入整个模块

```javascript
// JS：Node.js 内置模块
const os = require('os');
const path = require('path');
```

```python
# Python：import 语句
import os
import math

print(os.getcwd())   # 获取当前目录
print(math.pi)       # 圆周率
```

**关键点**：
- 用 `模块名.函数()` 的方式调用
- 不需要写文件后缀 `.py`

---

## 2. 导入特定内容

```javascript
// JS：解构导入
const { join } = require('path');
import { useState } from 'react';
```

```python
# Python：from ... import ...
from os.path import join

path = join("folder", "sub", "file.txt")  # folder\sub\file.txt
```

**关键点**：
- 直接用函数名，不需要 `模块名.`
- `join` 会自动使用系统路径分隔符（Windows 是 `\`，Mac/Linux 是 `/`）

---

## 3. 别名导入

```javascript
// JS：as 关键字
import { Component as Comp } from 'react';
```

```python
# Python：as 关键字
import json as j

data = j.dumps({"name": "小明", "age": 18}, ensure_ascii=False)
print(data)  # {"name": "小明", "age": 18}
```

**关键点**：
- `ensure_ascii=False` 让 JSON 保留中文原文，不转义成 `\uXXXX`

---

## 4. __name__ 的作用

```javascript
// JS：没有直接等价物
// Node.js 中可以用 require.main === module 判断
```

```python
# Python：__name__ 变量
print(__name__)  # 直接运行时输出 "__main__"

if __name__ == "__main__":
    print("只有直接运行时才执行")
```

| 情况 | `__name__` 的值 |
|------|----------------|
| 直接运行 `python xxx.py` | `"__main__"` |
| 被别人 import | `"模块名"` |

**用途**：把测试代码放在 `if __name__ == "__main__":` 里，导入时不会执行。

---

## 5. 创建自定义模块

```python
# helper.py — 自定义模块
def say_hi():
    print("hi!")

if __name__ == "__main__":
    # 测试代码，只在直接运行时执行
    say_hi()
```

```python
# 09_modules.py — 导入使用
import helper

helper.say_hi()  # 输出: hi!
```

**关键点**：
- 一个 `.py` 文件就是一个模块
- 文件名就是模块名

---

## 6. 常用内置模块速览

| 模块 | 用途 | JS 对应 |
|------|------|---------|
| `os` | 操作系统相关（文件、目录、环境变量） | `process`, `fs` |
| `sys` | Python 解释器相关（版本、路径） | `process` |
| `json` | JSON 序列化/反序列化 | `JSON` |
| `datetime` | 日期和时间处理 | `Date` |
| `math` | 数学函数 | `Math` |
| `random` | 随机数生成 | `Math.random()` |
| `pathlib` | 面向对象的路径操作 | `path` |
| `os.path` | 路径拼接、判断存在等 | `path` |

---

## 7. 速查表

| 操作 | JavaScript | Python |
|------|-----------|--------|
| 导入整个模块 | `const os = require('os')` | `import os` |
| 导入特定内容 | `const { join } = require('path')` | `from os.path import join` |
| 别名导入 | `import { a as b } from 'mod'` | `import mod as m` |
| 判断直接运行 | `require.main === module` | `if __name__ == "__main__":` |
| 创建模块 | 创建 `.js` 文件 | 创建 `.py` 文件 |

---

## 8. 注意事项

```python
# ❌ 导入不存在的模块
import nonexistent  # ModuleNotFoundError

# ✅ 查看模块搜索路径
import sys
print(sys.path)
```
