class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} 说 {self.sound}")
    
class Dog(Animal):
    def __init__(self, name, sound = "汪汪"):
        super().__init__(name, sound)

class Cat(Animal):
    def __init__(self, name, sound = "喵喵"):
        super().__init__(name, sound)

dog = Dog("小狗")
cat = Cat("小猫")
dog.speak()
cat.speak()


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def __str__(self): #print(student)时会调用这个方法
        return f"{self.name}({self.age}岁，成绩: {self.score})"
    
    def __eq__(self, other): #比较两个学生是否相等
        return self.name == other.name and self.age == other.age 
    

# 属性装饰器
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def area(self):
        return self._width * self._height
    
sample = Rectangle(5, 10)
print(sample.area)

#私有属性
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            print("余额不足")
        else:
            self.__balance -= amount
    @property
    def balance(self):
        return self.__balance
    
acc = BankAccount("小明", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)
#print(acc.__balance) #会报错，因为__balance是私有属性，不能直接访问