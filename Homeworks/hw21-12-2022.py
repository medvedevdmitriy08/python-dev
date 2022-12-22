# Домашнее задание от 21.12.2022 Медведев Дмитрий
# Пользователь вводит порядковый номер месяца c 1 и программа выводит к какому сезону относится данный месяц(осень, лето, зима, весна)

print('Эта программа расчитывает к какому сезону относится месяц.')
print('Для рассчёта пожалуйста введите ниже порядковый номер месяца (от 1 - январь до 12 - декабрь)')
while True:
    month = int(input())
    if month >= 1 and month <= 2 or month == 12:
        season = 'Зима'
        print(season)
    elif month >= 3 and month <= 5:
        season = 'Весна'
        print(season)
    elif month >= 6 and month <= 8:
        season = 'Лето'
        print(season)
    elif month >= 9 and month <= 11:
        season = 'Осень'
        print(season)
    else:
        print('Вы ввели неверный номер месяца!')