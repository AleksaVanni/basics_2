"""
Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4
"""

first_user = int(input('Введите количество элементов для первого списка: '))
first_lst = []

for i in range(first_user):
    element = int(input(f"Введите {i+1} элемент: "))
    first_lst.append(element)

second_user = int(input('Введите количество элементов для второго списка: '))
second_lst = []
for i in range(second_user):
    element = int(input(f"Введите {i+1} элемент: "))
    second_lst.append(element)
print()
print("Первый список: ", first_lst)
print("Второй список: ", second_lst)

for el in second_lst:
    if el in first_lst:
        first_lst.remove(el)
print("Результат: ", first_lst)
