import sys

f_obj, name_v, rate_v, house_v = sys.argv
print(f_obj)

def calculate_salary(rate, hours):
    try:
        print(f'Сотрудник {name_v} заработал {int(rate) * int(hours) * 1.5}')
    except TypeError:
        print("Операция применена к объекту несоответствующего типа")
        exit()

calculate_salary(rate_v, house_v)
