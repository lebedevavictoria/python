from functools import reduce

primary_list = [x for x in range(100, 1001, 2)]

print(primary_list)

res = reduce(lambda item, item2: item * item2, primary_list)

print(f"Результат: {res}")