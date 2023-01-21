def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('Введите аргумент 1:')),
    int(input('Введите аргумент 2:')),
    int(input('ВВедите аргумент 3:')),
)

