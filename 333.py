month = int(input("Введите пожалуйста номер месяца от 1 до 12 : "))
mlist = ["зима", "весна", "лето", "осень"]
while True:
    if month > 12 or month <= 0 :
        print(f"\tНеверный номер месяца!!! \n\tПожалуйста, используйте числа от 1 до 12!")
        month = int(input("ведите пожалуйста номер месяца от 1 до 12  : "))
        continue
    mlist = ["зима", "весна", "лето", "осень"]
    if month == 12 or (month >= 1 and month < 3):
        print(f"\tМесяц с номером {month}  это '{mlist[0]}'")
        break
    elif month >= 3 and month < 6:
        print(f"\tМесяц с номером {month} это '{mlist[1]}'")
        break
    elif month >= 6 and month < 9:
        print(f"\tМесяц с номером {month} это '{mlist[2]}'")
        break
    elif month >= 9 and month < 12:
        print(f"\tМесяц с номером {month} это '{mlist[3]}'")
        break