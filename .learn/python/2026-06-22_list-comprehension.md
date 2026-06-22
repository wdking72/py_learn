# 列表推导式笔记

## 1. 基本语法

```javascript
// JS：map
const nums = [1, 2, 3, 4];
const doubled = nums.map(n => n * 2);
```

```python
# Python：列表推导式
nums = [1, 2, 3, 4]
doubled = [n * 2 for n in nums]
# [2, 4, 6, 8]
```

**格式**：`[表达式 for 变量 in 列表]`

**区别**：JS 需要 `.map()`，Python 用 `[]` 一行搞定。

---

## 2. 带条件过滤

```javascript
// JS：filter + map 链式调用
const nums = [1, 2, 3, 4, 5, 6];
const evens = nums.filter(n => n % 2 === 0).map(n => n * 2);
```

```python
# Python：加 if 即可
nums = [1, 2, 3, 4, 5, 6]
evens = [n * 2 for n in nums if n % 2 == 0]
# [4, 8, 12]
```

**格式**：`[表达式 for 变量 in 列表 if 条件]`

**区别**：JS 需要 `filter` + `map` 两步，Python 一个 `[]` 搞定。

---

## 3. 嵌套展平

```javascript
// JS：flat() 或 flatMap()
const matrix = [[1, 2], [3, 4], [5, 6]];
const flat = matrix.flat();
```

```python
# Python：两层 for
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in matrix for n in row]
# [1, 2, 3, 4, 5, 6]
```

**格式**：`[表达式 for 外层变量 in 外层列表 for 内层变量 in 内层变量]`

**读法**：从左到右，对于每一行 `row`，再取出每个 `n`。

---

## 4. 字典推导式

```javascript
// JS：Object.fromEntries + map
const nums = [1, 2, 3];
const squares = Object.fromEntries(nums.map(n => [n, n * n]));
// {1: 1, 2: 4, 3: 9}
```

```python
# Python：字典推导式
nums = [1, 2, 3]
squares = {n: n * n for n in nums}
# {1: 1, 2: 4, 3: 9}
```

**格式**：`{key: value for 变量 in 列表}`

---

## 5. 速查表

| 类型 | 语法 | 例子 |
|---|---|---|
| 列表推导 | `[x for x in list]` | `[n * 2 for n in nums]` |
| 带过滤 | `[x for x in list if 条件]` | `[n for n in nums if n % 2 == 0]` |
| 嵌套展平 | `[x for row in matrix for x in row]` | |
| 字典推导 | `{k: v for x in list}` | `{n: n*n for n in nums}` |

---

## 6. 注意事项

```python
# ❌ 不要覆盖内置名称
list = [1, 2, 3]       # 覆盖了 list 类型
len = [1, 2, 3]        # 覆盖了 len() 函数

# ✅ 用有意义的变量名
nums = [1, 2, 3]
lengths = [len(word) for word in words]
```
