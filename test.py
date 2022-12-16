from random import randint

secret_number = randint(1, 10) # ЭТО рандомное число в диапазоне от 1 до 10
attemps = 3

print('Это программа угадай число. У вас 3 попытки, чтобы отгадать число')

while attemps > 0:

    print('Попыток: ' + str(attemps))
    attemps = attemps - 1

    number = int(input('Введите число: '))

    if number > secret_number:
        print('Слишком большое число')
    if number < secret_number:
        print('Слишком маленькое число')
    if number == secret_number:
        print('Молодец, угадал')
        break
    if attemps == 0:
        print('Ты проиграл, настоящее число: ' + str(secret_number))

