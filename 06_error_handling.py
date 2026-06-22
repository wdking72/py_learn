try: 
    x = 1 / 0
except ZeroDivisionError as e: 
    print(f"错误：{e}")

nums = [1, 2, 3]
try:
    print(nums[10])
except IndexError as e:
    print(f"错误：{e}")

try:
    int('44')
except ValueError as e:
    print(f"错误{e}")
else:
    print("转换成功")
finally:
    print("总是打印")

def set_age (age) :
    if (age < 0):
        raise ValueError ("年龄必须大于零")
    else:
        return age
try:    
    set_age(-2)
except ValueError as e:
    print(e)

# 自定义错误类
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"余额不足：需要{amount}，只有{balance}")

class Wallet:
    def __init__(self, money):
        self.money  = money
    def pay(self, amount):
        if(self.money < amount):
            raise InsufficientFundsError(self.money, amount)
        else:
            self.money -= amount
try:
    my_wallet = Wallet(100)
    my_wallet.pay(150)
except InsufficientFundsError as e:
    print(e)