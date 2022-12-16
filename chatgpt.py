from users import users, admins

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

def register():
    # Prompt the user to enter a username and password
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    
    # Check if the username is already taken
    if username in users:
        print('Извините, имя пользователя уже занято. Пожалуйста, выберите другое.')
        welcome()
        return
    
    # Add the new user to the users dictionary
    users[username] = password
    print('Вы успещно зарегистрировались!')
    login_as()
    return

def alogin(username, password):
    # Add input validation for username
    if not username:
        print('Имя пользователя не может быть пустым!')
        return
    if not username.isalnum():
        print('Имя пользователя может содержать только буквы и цифры!')
        return
    
    # Add input validation for password
    if not password:
        print('Пароль не может быть пустым!')
        return
    
    # Check if provided username and password are valid
    if username not in admins:
        print('Неверное имя пользователя или пароль!')
        return
    if password != admins[username]:
        print('Неверное имя пользователя или пароль!')
        return
    
    # Welcome the user and allow them to view the user database or log out
    print('Добро пожаловать,', username)
    while True:
        action = input('Выберите действие (1 - посмотреть БД пользователей, 0 - выйти) -> ')
        if action == '1':
            print('База данных пользователей')
            for user, passwd in users.items():
                print('Имя: ' + user + ', ' 'пароль: ' + passwd)
        if action == '0':
            welcome()
            return

def login(username, password):
    # Add input validation for username
    if not username:
        print('Имя пользователя не может быть пустым!')
        return
    if not username.isalnum():
        print('Имя пользователя может содержать только буквы и цифры!')
        return
    
    # Add input validation for password
    if not password:
        print('Пароль не может быть пустым!')
        return
    
    # Check if provided username and password are valid
    if username not in users:
        print('Неверное имя пользователя или пароль!')
        return
    if password != users[username]:
        print('Неверное имя пользователя или пароль!')
        return
    
    print('Добро пожаловать,', username)
    action = input('Выберите действие (0 - выйти) -> ')
    if action == '0':
        welcome()
        return
    else:
        return

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

welcome()