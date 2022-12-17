from mysql.connector import connect, Error
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
        username = input('Введите имя пользователя: ')
        password = getpass('Введите пароль: ')
        login(username, password)
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
    # Prompt the user to enter a username and password
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

    # Проверка не занято ли имя пользователя
    try:
        with connect(
            host='localhost',
            user='root',
            password='root',
            database='users'
        ) as connection:
            check_username = '''
                SELECT * FROM `users` WHERE `Username`='{}'
            '''.format(username)
            with connection.cursor() as cursor:
                cursor.execute(check_username)
                if cursor.fetchone():
                    print('Извините, имя пользователя уже занято, выберите другое.')
                    welcome()
                    return
            # Добавляет нового пользователя в БД
            add_user = '''
                INSERT INTO `users` (`Username`, `Password`)
                VALUES ('{}', '{}')
            '''.format(username, password)
            with connection.cursor() as cursor:
                cursor.execute(add_user)
            connection.commit()
            print('Вы успешно зарегистрировались!')
            welcome()
            return
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

'''
Логин
'''
def login(username, password):
    try:
        with connect(
            host='localhost',
            user='root',
            password='root',
            database='users'
        ) as connection:
            # Проверка на существование такого аккаунта
            check = '''
                SELECT * FROM `users` WHERE `Username`='{}' AND `Password`='{}'
            '''.format(username, password)
            with connection.cursor() as cursor:
                cursor.execute(check)
                if not cursor.fetchone():
                    print('Неверное имя пользователя или пароль!')
                    welcome()
                    return
            check_ban = '''
                SELECT * FROM `users` WHERE `Username`='{}' AND `Ban`='True'
            '''.format(username)
            with connection.cursor() as cursor:
                cursor.execute(check_ban)
                if cursor.fetchone():
                    print('Ваш аккаунт был заблокирован администрацией!')
                    welcome()
                    return
            check_admin = '''
                SELECT * FROM `users` WHERE `Username`='{}' AND `Admin`='True'
            '''.format(username)
            with connection.cursor() as cursor:
                cursor.execute(check_admin)
                if cursor.fetchone():
                    print('Добро пожаловать, ', username)
                    a_session()
                    return
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

    print('Добро пожаловать, ', username)
    u_session()
    return

'''
Сессия пользователя
'''
def u_session():
    action = input('Выберите действие (0 - выйти) -> ')
    if action == '0':
        welcome()
        return
    else:
        welcome()
        return
'''
Сессия админа
'''
# Поприветствуйте пользователя и разрешите ему выполнить действия или выйти из системы
def a_session():
    print('Выберите действие: 1 - посмотреть БД пользователей, 2 - добавить пользователя, 3 - удалить пользователя,' +  
    '4 - изменить статус блокировки пользователя,\n5 - выдать/снять админ-права (ОСТОРОЖНО), \n 0 - выйти'
    
    )
    action = input('-> ')
    if action == '1':
        print('Вот база данных всех зарегистрированых пользователей:')
        see_db()
        return
    elif action == '2':
        username = input('Придумайте имя: ')
        password = input('Придумайте пароль: ')
        add_user(username, password)
        return
    elif action == '3':
        id = input('Введите ID пользователя из базы данных: ')
        del_user(id)
        return
    elif action == '4':
        id = input('Введите ID пользователя из базы данных: ')
        a = input('Выберите действие (1 - выдать блокировку, 0 - снять блокировку): ')
        ban(id, a)
        return
    elif action == '5':
        id = input('Введите ID пользователя из базы данных: ')
        a = input('Выберите действие (1 - выдать права, 0 - снять права): ')
        makeadmin(id, a)
        return
    elif action == '0':
        welcome()
        return
    else:
        print('Выбрано неверное действие!')
        welcome()
        return
'''
Действия админа
'''
def add_user(username, password):
    try:
        with connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'users',
        ) as connection:
            check_username = '''
                SELECT * FROM `users` WHERE `Username`='{}'
            '''.format(username)
            with connection.cursor() as cursor:
                cursor.execute(check_username)
                if cursor.fetchone():
                    print('Имя пользователя уже занято, выберите другое.')
                    a_session()
                    return
            add_user = '''
                INSERT INTO `users`.`users` (`Username`, `Password`)
                VALUES ('{}', '{}')
            '''.format(username, password)
            with connection.cursor() as cursor:
                cursor.execute(add_user)
            connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
    
    print('Вы успешно создали пользователя!')
    a_session()
    return

def see_db():
    try:
        with connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'users',
        ) as connection:
            database = '''
                SELECT * FROM `users`
            '''
            with connection.cursor() as cursor:
                cursor.execute(database)
                for row in cursor.fetchall():
                    print(row)
            connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
    
    a_session()
    return

def del_user(id):
    try:
        with connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'users',
        ) as connection:
            check_username = '''
                SELECT * FROM `users` WHERE `ID`={}
            '''.format(id)
            with connection.cursor() as cursor:
                cursor.execute(check_username)
                if not cursor.fetchone():
                    print('Такого аккаунта не существует!')
                    a_session()
                    return
            del_user = '''
                DELETE FROM `users`.`users` WHERE `ID` = {}
            '''.format(id)
            with connection.cursor() as cursor:
                cursor.execute(del_user)
            connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
    
    print('Вы успешно удалили пользователя!')
    a_session()
    return

def ban(id, a):
    try:
        with connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'users',
        ) as connection:
            check_username = '''
                SELECT * FROM `users` WHERE `ID`={}
            '''.format(id)
            with connection.cursor() as cursor:
                cursor.execute(check_username)
                if not cursor.fetchone():
                    print('Такого аккаунта не существует!')
                    a_session()
                    return

            if a == '1':
                ban_user = '''
                    UPDATE `users`.`users` SET `Ban` = 'True' WHERE `ID` = {}
                '''.format(id)
                with connection.cursor() as cursor:
                    cursor.execute(ban_user)
                connection.commit()
                print('Вы успешно збанили пользователя!')
                a_session()
                return
            elif a == '0':
                unban_user = '''
                    UPDATE `users`.`users` SET `Ban` = 'False' WHERE `ID` = {}
                '''.format(id)
                with connection.cursor() as cursor:
                    cursor.execute(unban_user)
                connection.commit()
                print('Вы успешно разбанили пользователя!')
                a_session()
                return
            else:
                print('Неверное действие')
                a_session()
                return
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

def makeadmin(id, a):
    try:
        with connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'users',
        ) as connection:
            check_username = '''
                SELECT * FROM `users` WHERE `ID`={}
            '''.format(id)
            with connection.cursor() as cursor:
                cursor.execute(check_username)
                if not cursor.fetchone():
                    print('Такого аккаунта не существует!')
                    a_session()
                    return

            if a == '1':
                ban_user = '''
                    UPDATE `users`.`users` SET `Admin` = 'True' WHERE `ID` = {}
                '''.format(id)
                with connection.cursor() as cursor:
                    cursor.execute(ban_user)
                connection.commit()
                print('Вы успешно сделали пользователя администратором!')
                a_session()
                return
            elif a == '0':
                unban_user = '''
                    UPDATE `users`.`users` SET `Admin` = 'False' WHERE `ID` = {}
                '''.format(id)
                with connection.cursor() as cursor:
                    cursor.execute(unban_user)
                connection.commit()
                print('Вы успешно сняли админ-права с пользователя!')
                a_session()
                return
            else:
                print('Неверное действие')
                a_session()
                return
    except Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

welcome()