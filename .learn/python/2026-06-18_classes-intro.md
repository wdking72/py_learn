# 类与继承笔记

## 1. 类的写法

```python
class User:
    def __init__(self, name, age):    # 构造函数固定叫 __init__
        self.name = name              # self 类似 JS 的 this
        self.age = age

    def greet(self):                  # 方法必须带 self 参数
        return f"我是{self.name}，{self.age}岁"

user = User("Alice", 25)             # 不需要 new
```

## 2. 与 JS 的区别

| JS | Python | 说明 |
|---|---|---|
| `constructor()` | `__init__(self)` | 构造函数 |
| `this.name` | `self.name` | 实例引用 |
| `new User()` | `User()` | 不需要 new |
| `class Dog extends Animal` | `class Dog(Animal):` | 继承写法 |

---

## 3. 继承

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} 说 {self.sound}")

class Dog(Animal):                    # 括号里写父类名
    def __init__(self, name, sound="汪汪"):
        super().__init__(name, sound) # super() 调用父类构造函数
```

---

## 4. 魔术方法（Magic Methods）

双下划线包裹的方法，Python 会在特定场景自动调用。

| 魔术方法 | 触发时机 | JS 等价 |
|---|---|---|
| `__str__` | `print(对象)` | `toString()` |
| `__repr__` | 终端直接输入对象 | 无 |
| `__eq__` | `对象1 == 对象2` | 无（JS用===比引用） |
| `__lt__` | `对象1 < 对象2` | 无（用于排序） |

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):    # 必须 return 字符串，不能 print
        return f"{self.name}({self.age}岁，成绩:{self.score})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

s1 = Student("小明", 20, 85)
s2 = Student("小明", 20, 90)
print(s1)        # → 小明(20岁，成绩:85)
print(s1 == s2)  # → True（名字和年龄相同）
```

---

## 5. @property 属性装饰器

把方法变成属性访问，不需要加括号 `()`。

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property                # 像属性一样访问：rect.area
    def area(self):
        return self._width * self._height

rect = Rectangle(5, 3)
print(rect.area)    # 不是 rect.area()
```

| JS | Python |
|---|---|
| `get area() { ... }` | `@property` |

---

## 6. 私有属性

用 `__` 双下划线前缀隐藏内部数据，外部不能直接访问。

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # 私有属性

    @property
    def balance(self):                # 用 property 只读暴露
        return self.__balance

acc = BankAccount("小明", 1000)
print(acc.balance)      # ✅ 通过 property 访问
# print(acc.__balance)  # ❌ AttributeError（不能直接访问）
```

| JS | Python |
|---|---|
| `#balance` | `__balance` |

---

## 7. 命名规范

- 类名：`PascalCase`（如 `BankAccount`）
- 变量/方法：`snake_case`（如 `get_balance`）
- 私有属性：`__` 前缀（如 `__balance`）
- 保护属性：`_` 前缀（如 `_width`，约定俗成，不强制）
