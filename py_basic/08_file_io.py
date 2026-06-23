import os
with open("test.txt", "w") as f:
    f.write("你好 Python" \
    "111" \
    "222\n33")


with open("test.txt", 'r') as f :
    line = f.readlines() # readlines()返回列表
print(line)
with open("test.txt", 'r') as f :
    for line in f:
        print(line.strip()) # strip() 去掉末尾换行符

with open("test.txt", "a") as f :
    f.write("追加的内容")

with open("test.txt", 'r') as f :
    content = f.read()
print(content)

if os.path.exists("test.txt"):
    print("文件存在")

try:
    with open("jxijda", "r") as f:
        content =f.read()
except FileNotFoundError:
    print("文件不存在")
