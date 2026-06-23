print(f"helper的__name__：{__name__}")

def say_hi():
    print("hi")

if __name__ == "__main__":
    print("我是测试代码，只有直接运行 helper.py 才会执行")