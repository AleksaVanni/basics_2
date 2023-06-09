"""
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') -
предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей,
это можно реализовать с помощью модуля random и функции sample
После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'
Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ,
но уже в следующем виде: третье января 2009 года, склонением можно пренебречь
В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
"""

import random

print('Игра "Викторина"')

play_again = 'да'
while play_again == 'да':
    print('Ответьте на вопросы:')
    print("Введите дату рождения в формате - 'dd.mm.yyyy'")
    print('*' * 20)

    birthdays = {'Александр Суворов': '24.11.1729',
                 'Альберт Эйнштейн': '14.03.1879',
                 'Гагарин Юрий': '09.03.1934',
                 'Исаак Ньютон': '04.01.1643',
                 'Менделеев Д.И.': '08.02.1834',
                 'Михаил Кутузов': '16.09.1745',
                 'Петр I': '09.06.1672',
                 'Пушкин А.С.': '26.05.1799',
                 'Путин В.В.': '07.10.1952',
                 'Сергей Есенин': '03.10.1895'
                 }

    months = {'01': "января",
              '02': "февраля",
              '03': "марта",
              '04': "апреля",
              '05': "мая",
              '06': "июня",
              '07': "июля",
              '08': "августа",
              '09': "сентября",
              '10': "октября",
              '11': "ноября",
              '12': "декабря"
              }

    days_month = {'01': 'первого', '02': 'второго', '03': 'третьего', '04': 'четвёртого', '05': 'пятого',
                  '06': 'шестого', '07': 'седьмого', '08': 'восьмого', '09': 'девятого', '10': 'десятого',
                  '11': 'одиннадцатого', '12': 'двенадцатого', '13': 'тринадцатого', '14': 'четырнадцатого',
                  '15': 'пятнадцатого',
                  '16': 'шестнадцатого', '17': 'семнадцатого', '18': 'восемнадцатого', '19': 'девятнадцатого',
                  '20': 'двадцатого',
                  '21': 'двадцать первого', '22': 'двадцать второго', '23': 'двадцать третьего',
                  '24': 'двадцать четвертого', '25': 'двадцать пятого',
                  '26': 'двадцать шестого', '27': 'двадцать седьмого', '28': 'двадцать восьмого',
                  '29': 'двадцать девятого',
                  '30': 'тридцатого', '31': 'тридцать первого'
                  }

    random_birthdays = random.sample(list(birthdays.keys()), 5)
    correct = 0
    error = 0

    for person in random_birthdays:
        questions_data = input(f"Когда родился {person} ('dd.mm.yyyy')?: ")
        if questions_data == birthdays[person]:
            correct += 1
            print(f'Правильно!')
        else:
            error += 1
            day, month, year = birthdays[person].split('.')
            print(f'Неправильно! {person} родился: {days_month[day]} {months[month]} {year} года')

    print('*' * 20)
    print('Подсчет баллов:')
    print("Правильных ответов: ", correct)
    print("Количество неправильных ответов: ", error)

    play_again = input("Хотите сыграть еще раз? ('да'/'нет'): ")

print('конец викторины')