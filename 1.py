def div(*args):

    try:
        arg1 = int(input("Введите делимое "))
        arg2 = int(input("Введите делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

    return res

    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Значение не может быть равно нулю")

print(f'result  {div()}')