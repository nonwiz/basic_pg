
def signup():
    username = input('Input username:')
    if username in user:
        print('This username exists already!')
        return
    passwd = input('Input password:')
    user[username] = passwd 
    print('A new user is created successfully!')

def display_user():
    for u in user:
        print(' -> username:', u, '|| password:', user[u])

def login():
    username = input('Username:')
    passwd = input('Password:')
    if username in user and user[username] == passwd:
        print('*'*100)
        print('Welcome to user dashboard \nHere is a list of created users')
        display_user()
        return
    print('Username or password is incorrect!')

user,  option = {}, {'1': signup, '2': login}

while True:
    choice = input('(1) Signup \n(2) Login \nInput your choice:')
    if choice in option:
        option.get(choice)()
    else: 
        print('Option Invalid!')
    print('*'*100)