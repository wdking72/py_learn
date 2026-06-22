# 错误处理笔记

## 1. 基本语法

```javascript
// JS：try/catch
try {
    let result = 10 / 0;
} catch (e) {
    console.log(e.message);
}
```

```python
# Python：try/except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"错误：{e}")
```

**区别**：`catch` → `except`，用 `as` 绑定错误对象。

---

## 2. 多种错误类型

```javascript
// JS：只能一个 catch，需要自己判断类型
try {
    JSON.parse("abc");
} catch (e) {
    if (e instanceof SyntaxError) {
        console.log("语法错误");
    } else {
        console.log("其他错误");
    }
}
```

```python
# Python：多个 except 分别处理
try:
    nums = [1, 2, 3]
    print(nums[10])
except IndexError as e:
    print(f"索引错误：{e}")
except TypeError as e:
    print(f"类型错误：{e}")
```

也可以合并捕获：

```python
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(f"值或类型错误：{e}")
```

**区别**：Python 可以写多个 `except`，每种错误单独处理，比 JS 更清晰。

---

## 3. else 和 finally

```python
try:
    num = int("42")
except ValueError:
    print("转换失败")
else:
    print(f"转换成功：{num}")   # 只有没出错才执行
finally:
    print("总是执行")           # 无论如何都执行
```

| 关键字 | 时机 | JS 有吗 |
|---|---|---|
| `else` | 没出错时执行 | ❌ 没有 |
| `finally` | 总是执行 | ✅ 一样 |

---

## 4. 抛出错误

```javascript
// JS
throw new Error("出错了");
throw new TypeError("类型不对");
```

```python
# Python：raise 错误类型("信息")
raise ValueError("年龄不能为负数")
raise TypeError("类型不对")
```

**区别**：`throw new Error()` → `raise ValueError()`。

---

## 5. 自定义错误类

```javascript
// JS
class InsufficientFundsError extends Error {
    constructor(balance, amount) {
        super(`余额不足：需要 ${amount}，只有 ${balance}`);
        this.balance = balance;
        this.amount = amount;
    }
}
```

```python
# Python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"余额不足：需要 {amount}，只有 {balance}")
```

**区别**：`extends Error` → `Exception`，写法几乎一样。

---

## 6. 实际应用

```python
# 自定义错误配合类使用
class Wallet:
    def __init__(self, money):
        self.money = money

    def pay(self, amount):
        if amount > self.money:
            raise InsufficientFundsError(self.money, amount)
        self.money -= amount

wallet = Wallet(100)
try:
    wallet.pay(150)
except InsufficientFundsError as e:
    print(e)           # 余额不足：需要 150，只有 100
```
