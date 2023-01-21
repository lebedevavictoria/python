revenue = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))
if revenue > costs:
    print('Организациия работает в прибыль')
    profitability = (revenue - costs) / revenue
    print(f'Рентабельность доходов организации составляет: {profitability}')
elif revenue < costs:
    print('Организация работает в убыток')
else:
    print('Издержки организации равны доходам')