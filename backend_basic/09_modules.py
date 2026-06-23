import os
import math
from os.path import join
import json as j

print(os.getcwd()) # 获取目录
print(math.pi) # 圆周率

path = join("floder", "sub", "file.txt")
print(path)

data1 = j.dumps({"name": "小明", "age": 18}, ensure_ascii=False)
data2 = j.dumps({"name": "小明", "age": 18})
print(data1, data2)


print(__name__)
if __name__ == "__main__":
    print("我是直接运行的")

import helper