apassword = '12022'

database = ['M', 'Az2', 'Chris', '324565', 'ADMIN', '12022'] # База данных пользователей

'''
Блок функции администратора
'''

def login_in(apass):
    while apass == apassword:
        action = input('Выберите действие (1 - посмотреть базу данных, 0 - выйти из системы) -> ')

        if action == '1':
            print('Вот список всех зарегистрированых пользователей и их пароли:')
            for i in database:
                print(i)
        if action == '0':
            break

    else:
        print('Вы ввели неверный админ-пароль!')
        return
            
'''
Блок функции входа
'''
def login_as(cont):
    if cont == '1':
        print('К сожалению регистрация пользователей сейчас недоступна')
        return
    elif cont == '2':
        print('Здравствуйте, администратор. Введите админ-пароль чтобы войти в систему')
        upass = input()
        login_in(upass)

cont = input('Выберите, как хотите войти (1 - пользователь, 2 - администратор) -> ')
login_as(cont)