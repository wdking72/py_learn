# Python vs JavaScript 语法速成笔记

## 1. 变量

```javascript
// JS：需要声明关键字
let name = "Alice";
const age = 25;
```

```python
# Python：直接赋值，无需关键字
name = "Alice"
age = 25
```

**区别**：Python 没有 `let`/`const`/`var`，变量名直接写。

---

## 2. 类型系统

| JS | Python | 说明 |
|---|---|---|
| `string` | `str` | |
| `number` | `int` / `float` | Python 区分整数和浮点数 |
| `boolean` | `bool` | `True`/`False` 首字母大写 |
| `null` | `None` | |
| `undefined` | ❌ 不存在 | Python 没有 undefined |

---

## 3. 字符串插值

```javascript
// JS：模板字符串
console.log(`Hello, ${name}!`);
```

```python
# Python：f-string
print(f"Hello, {name}!")
```

---

## 4. 条件判断

```javascript
// JS
if (age >= 18) {
    console.log("成年");
} else if (age >= 12) {
    console.log("青少年");
} else {
    console.log("儿童");
}
```

```python
# Python
if age >= 18:
    print("成年")
elif age >= 12:    # else if → elif
    print("青少年")
else:
    print("儿童")
```

**区别**：
- `else if` → `elif`
- 没有 `{}`，用 `:` + 缩进（4 空格）
- 条件不需要括号

---

## 5. 循环

```javascript
// JS：for...of
for (const skill of skills) {
    console.log(skill);
}
```

```python
# Python：for...in
for skill in skills:
    print(skill)

# 带索引
for i, skill in enumerate(skills):
    print(f"{i}: {skill}")
```

**区别**：
- `for...of` → `for...in`
- 带索引用 `enumerate()`，不需要手动 `i++`

---

## 6. 数据结构对比

### 列表 vs 数组
```javascript
const skills = ["js", "py"];
skills.push("rust");       // push
skills.length;             // length
```

```python
skills = ["js", "py"]
skills.append("rust")      # append
len(skills)                # len()
```

### 字典 vs 对象
```javascript
const user = { name: "Alice", age: 25 };
user.name;                 // 点访问
user["name"];              // 括号访问
delete user.age;           // delete
```

```python
user = {"name": "Alice", "age": 25}
user["name"]               # 只能括号访问
user.get("name")           # .get() 更安全，不存在返回 None
del user["age"]            # del
```

**区别**：Python 字典**没有点访问**，只能用 `["key"]` 或 `.get("key")`。

### 元组（Python 独有）
```python
point = (3, 5)      # 不可修改
x, y = point        # 解包
```

---

## 7. 函数

```javascript
// JS：多种写法
function greet(name) { return `Hello, ${name}`; }
const add = (a, b) => a + b;
```

```python
# Python：只有一种
def greet(name):
    return f"Hello, {name}"

def add(a, b):
    return a + b
```

**区别**：
- 用 `def` 定义，没有箭头函数
- 默认参数直接写在定义里：`def greet(name, greeting="你好")`
- `*args` 接收不定位置参数（元组），`**kwargs` 接收不定关键字参数（字典）

---

## 8. 命名规范

| 风格 | JS | Python |
|---|---|---|
| 变量/函数 | `camelCase` | `snake_case` |
| 常量 | `UPPER_CASE` | `UPPER_CASE` |
| 类 | `PascalCase` | `PascalCase` |

---

## 9. 缩进

JS 用 `{}` 划分代码块，缩进只是风格。Python 用缩进划分代码块，缩进错误会报错。统一用 **4 个空格**。
