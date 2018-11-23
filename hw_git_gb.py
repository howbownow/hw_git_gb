import random

choice_list = input('Введите список ').split()

print('Выбираем из: ')
for elem in choice_list:
    print(elem, end=', ')

print('\nСлучайный элемент:', random.choice(choice_list))
