def calculate_area(width, height):
    return width * height
def create_user(name, age, email = "未填写"):
    return {"name": name, "age": age, "email": email}

area = calculate_area(10, 20)
print(f"矩形的面积是：{area}")
user1 = create_user("wdking", 18)
print(user1)

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
result = sum_all(1, 2, 3, 4, 5)
print(f"所有数字的和是：{result}")