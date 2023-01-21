from itertools import count

def fact(n):

    factorial = 1

    for x in count (1):
        if x > n:
            break

        factorial = factorial * x
        yield factorial

n = int(input("Укажите целое неотрицательное число>>> "))
i = 0

for el in fact(n):
    i += 1
    print(f"!{i} = {el}")
