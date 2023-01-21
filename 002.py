entered_time = int(input('Напишите время в секундах: '))

hours = entered_time // 3600
minutes = (entered_time - hours * 3600) // 60
seconds = (entered_time - hours * 3600) - minutes * 60
print(f'{hours}:{minutes}:{seconds}')