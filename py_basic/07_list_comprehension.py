nums = [1, 2, 3]
new_nums = [num * 3 for num in nums]
print(new_nums)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n * 2 for n in numbers if n % 2 == 0]
print(evens)

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in matrix for n in row]
print(flat)

dic = ["apple", "banana", "cherry"]
lens = {key: len(key) for key in dic}
print(lens)