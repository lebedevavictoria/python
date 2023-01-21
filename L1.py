with open('new_file1.txt', 'a') as file:
    while True:
        user_answ = input('Напишите текст: ')
        file.write(user_answ + '\n')
        if not user_answ:
            break