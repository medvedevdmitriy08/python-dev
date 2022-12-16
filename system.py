from users import users, admins

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
    password = input('Введите пароль: ')

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
        password = input('Введите пароль: ')
        login(username, password)
        return
    elif cont == '2':
        username = input('Введите имя пользователя: ')
        password = input('Введите пароль: ')
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
        return
    if not username.isalnum():
        print('Имя пользователя может содержать только буквы и цифры!')
        return
    
    # Добавить проверку ввода пароля
    if not password:
        print('Пароль не может быть пустым!')
        return
    
    # Проверьте, действительны ли предоставленные имя пользователя и пароль
    if username not in users:
        print('Неверное имя пользователя или пароль!')
        return
    if password != users[username]:
        print('Неверное имя пользователя или пароль!')
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
        return
    if not username.isalnum():
        print('Имя пользователя может содержать только буквы и цифры!')
        return
    
    # Добавить проверку ввода пароля
    if not password:
        print('Пароль не может быть пустым!')
        return
    
    # Проверьте, действительны ли предоставленные имя пользователя и пароль
    if username not in admins:
        print('Неверное имя пользователя или пароль!')
        return
    if password != admins[username]:
        print('Неверное имя пользователя или пароль!')
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
    print('Выберите действие (1 - посмотреть БД пользователей, 2 - добавить пользователя, 3 - удалить пользователя, 4 - сменить пользователю пароль, 0 - выйти)')
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
    elif action == '0':
        login_as()
        return
'''
Действия админа
'''
def see_u_db():
    print('База данных пользователей')
    for user, passwd in users.items():
        print('Имя: ' + user + ', ' 'пароль: ' + passwd)
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

welcome()