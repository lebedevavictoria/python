rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('file_3.txt', 'r', encoding='UTF-8') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ')
    print(new_file)

with open('file_7.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)