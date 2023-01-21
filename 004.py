n = int(input('Напишите целое положительное число: '))

max = n % 10
while True:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    elif n > 9:
        continue
    else:
        print(f'Самая большая цифра в числе: {max}')
        break