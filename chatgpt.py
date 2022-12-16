admins = {
    'M': 'qwertyU0',
    'Az2': 'qwertyU0',
    'Chris': 'qwertyU0',
    '324565': 'qwertyU0',
    'ADMIN': 'AzXc1202'
    }

users = {

}

def alogin(username, password):
    # Add input validation for username
    if not username:
        print('Username cannot be empty')
        return
    if not username.isalnum():
        print('Username can only contain letters and numbers')
        return
    
    # Add input validation for password
    if not password:
        print('Password cannot be empty')
        return
    
    # Check if provided username and password are valid
    if username not in admins:
        print('Invalid username')
        return
    if password != admins[username]:
        print('Incorrect password')
        return
    
    # Welcome the user and allow them to view the user database or log out
    print('Welcome,', username)
    while True:
        action = input('Enter 1 to view user database, 0 to log out -> ')
        if action == '1':
            print('Registered users and passwords:')
            for user, passwd in admins.items():
                print(user, passwd)
        if action == '0':
            return

cont = input('Choose how you want to log in (1 - user, 2 - administrator) -> ')
if cont == '1':
    print('User registration is currently unavailable')
else:
    username = input('Enter username: ')
    password = input('Enter password: ')
    alogin(username, password)