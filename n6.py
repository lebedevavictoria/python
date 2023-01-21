from itertools import count, cycle

list_int = []

a = int(input ("Укажите первое число последовательности>>>"))
n = int(input ("Укажите последнее число последовательности>>>"))

for x in count (a):
    if x > n:
        break
    print(x)
    list_int.append(x)

#b

print()
print(list_int)

count = 0
for item in cycle(list_int):
    if count >= len(list_int):
        break
    print(item)
    count += 1
