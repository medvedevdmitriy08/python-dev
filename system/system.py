from database import users, admins, ban
from getpass import getpass

'''
Начало
'''
def welcome():
    action = input('Выберите действие (1 - зарегистрироваться, 2 - войти, 0 - выйти) -> ')
    if action == '1':
        register()
        return
    elif action == '2':
        login_as()
        return
    elif action == '0':
        return
    else:
        print('Ошибка! Неверное действие!')
        return
'''
Регистрация
'''
def register():
    # Предложите пользователю ввести имя пользователя и пароль
    username = input('Введите имя пользователя: ')
    password = getpass('Введите пароль: ')

    # Проверка введёных данных
    if not username:
        print('Имя пользователя не может быть пустым!')
        return
    if not username.isalnum():
        print("Имя пользователя может содержать только буквы и цифры!")
        return
    if not password:
        print('Пароль не может быть пустым!')
        return
    if len(password) < 8:
        print("Пароль должен содержать минимум 8 символов!")
        return
    # Проверьте, занято ли уже имя пользователя
    if username in users:
        print('Извините, имя пользователя уже занято. Пожалуйста, выберите другое.')
        welcome()
        return
    
    # Добавьте нового пользователя в словарь пользователей
    users[username] = password
    ban[username] = 'False'
    print('Вы успешно зарегистрировались!')
    login_as()
    return
'''
Войти как
'''
def login_as():
    cont = input('Выберите, как вы хотите войти в систему (1 - пользователь, 2 - администратор, 0 - выход) -> ')
    if cont == '1':
        username = input('Введите имя пользователя: ')
        password = getpass('Введите пароль: ')
        login(username, password)
        return
    elif cont == '2':
        username = input('Введите имя пользователя: ')
        password = getpass('Введите пароль: ')
        alogin(username, password)
        return
    elif cont == '0':
        welcome()
        return
    else:
        return
'''
Логин пользователя
'''
def login(username, password):
    # Добавить проверку ввода для имени пользователя
    if not username:
        print('Имя пользователя не может быть пустым!')
        login_as()
        return
    if not username.isalnum():
        print('Имя пользователя может содержать только буквы и цифры!')
        login_as()
        return
    
    # Добавить проверку ввода пароля
    if not password:
        print('Пароль не может быть пустым!')
        login_as()
        return
    
    # Проверьте, действительны ли предоставленные имя пользователя и пароль
    if username not in users:
        print('Неверное имя пользователя или пароль!')
        login_as()
        return
    if password != users[username]:
        print('Неверное имя пользователя или пароль!')
        login_as()
        return

    if ban[username] == 'True':
        print('Ваш аккаунт был заблокирован!')
        login_as()
        return

    print('Добро пожаловать,', username)
    action = input('Выберите действие (0 - выйти) -> ')
    if action == '0':
        login_as()
        return
    else:
        return
'''
Логин админа
'''
def alogin(username, password):
    # Добавить проверку ввода для имени пользователя
    if not username:
        print('Имя пользователя не может быть пустым!')
        login_as()
        return
    if not username.isalnum():
        print('Имя пользователя может содержать только буквы и цифры!')
        login_as()
        return
    
    # Добавить проверку ввода пароля
    if not password:
        print('Пароль не может быть пустым!')
        login_as()
        return
    
    # Проверьте, действительны ли предоставленные имя пользователя и пароль
    if username not in admins:
        print('Неверное имя пользователя или пароль!')
        login_as()
        return
    if password != admins[username]:
        print('Неверное имя пользователя или пароль!')
        login_as()
        return
    
    # Поприветствуйте пользователя и разрешите ему выполнить действия или выйти из системы
    print('Добро пожаловать,', username)
    a_session()
    return

'''
Сессия админа
'''
# Поприветствуйте пользователя и разрешите ему выполнить действия или выйти из системы
def a_session():
    print('Выберите действие (1 - посмотреть БД пользователей, 2 - добавить пользователя, 3 - удалить пользователя, 4 - сменить пользователю пароль, 5 - блокировка пользователей,\n 0 - выйти)')
    action = input('-> ')
    if action == '1':
        see_u_db()
        return
    elif action == '2':
        username = input('Придумайте имя: ')
        password = input('Придумайте пароль: ')
        add_user(username, password)
        return
    elif action == '3':
        username = input('Введите имя пользователя, которого желаете удалить: ')
        delete_user(username)
        return
    elif action == '4':
        username = input('Введите пользователя, которому желаете изменить пароль: ')
        password = input('Введите новый пароль для этого пользователя: ')
        change_user_password(username, password)
        return
    elif action == '5':
        username = input('Введите имя пользователя, статус блокировки которого желаете изменить: ')
        act = input('Выберите действие (1 - выдать блокировку, 0 - снять блокировку): ')
        ban_user(username, act)
        return
    elif action == '0':
        login_as()
        return
    else:
        print('Выбрано неверное действие!')
        welcome()
        return
'''
Действия админа
'''
def see_u_db():
    print('База данных пользователей')
    for user, passwd in users.items():
        print('Имя: ' + user + ', пароль: ' + passwd)
    print('Список статуса блокировки пользователей')
    for user, status in ban.items():
        print('Имя: ' + user + ', статус: ' + status)
    a_session()
    return

def add_user(username, password):
    # Проверка на существование такого пользователя
    if username in users:
        print('Такой пользователь уже зарегистрирован. Выберите другое имя!')
        a_session()
        return
    # Добавляет нового пользователя в БД с уже установленым паролем
    users[username] = password
    ban[username] = 'False'
    print('Пользователь {} успешно добавлен'.format(username))
    a_session()
    return

def delete_user(username):
    # Проверка на существование такого пользователя
    if not username in users:
        print('Такого пользователя не существует!')
        a_session()
        return
    del users[username]
    del ban[username]
    print('Пользователь {} успешно удален'.format(username))
    a_session()
    return

def change_user_password(username, password):
    # Проверка на существование такого пользователя
    if not username in users:
        print('Такого пользователя не существует!')
        a_session()
        return
    users[username] = password
    print('Пароль пользователя {} успешно изменен'.format(username))
    a_session()
    return

def ban_user(username, act):
    # Проверка на существование такого пользователя
    if not username in users:
        print('Такого пользователя несуществует либо в БД пользователей, либо в БД статусов!')
        a_session()
        return
    if act == '1':
        ban[username] = 'True'
        print('Пользователю {} успешно выдана блокировка'.format(username))
        a_session()
        return
    elif act == '0':
        ban[username] = 'False'
        print('Пользователю {} успешно снята блокировка'.format(username))
        a_session()
        return
    else:
        print('Выбрано неверное действие!')
        a_session()
        return

welcome()