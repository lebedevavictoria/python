def info_user(name, surname, year_of_birth, city_of_residence, email, phone):
    print(f" {name} {surname} {year_of_birth}-го года рождения, проживает в городе {city_of_residence}, "
          f"Контактные данные:  Email {email} , номер телефона {phone}")


user_quest = {
    'name': 'Имя',
    'surname': 'Фамилия',
    'year_of_birth': 'Год рождения',
    'city_of_residence': 'Город проживания',
    'email': 'Email',
    'phone': 'Телефон'
}
my_user = {}
for key, value in user_quest.items():
    input_value = input(f'{value}: ')
    my_user.update({key: input_value})

info_user(**my_user)