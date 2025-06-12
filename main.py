# simple messaging system

# creating a empty dictionary which store username and their details
users = {}

# creating a function which add user and their details in user dictionary
def people(username,age,number):
    if age <= 13:
        print('You are under age for this system! (bachu)')
    if username not in users:
        users[username] = {'age': age, 'number': number}
        print(f'user is created with username {username}')
    else:
        print(f'You are already user with username of {username}')
    

# checking the profile of the user
def profile(username, detail = 'all'):
    if username not in users:
        print(f'user of username {username} is not registered with us! ')
    elif username in users and detail == 'age':
        print('Printing the detail of the user: ')
        print(f'the {detail} of the {username} == {users[username][detail]}')
    elif username in users and detail == 'number':
        print('Printing the detail of the user: ')
        print(f'the {detail} of the {username} == {users[username][detail]}')
    else:
        print(f'the details of user with username of {username} is here: \n age of the user  == {users[username]['age']} \n number of the user == {users[username]['number']}')

# creating a empty dictionary to store the sent message of the user
sent = {}
# creating a function to send message
def send(sender,reciver,message):
    if sender not in users:
        print(f'You are not registred with us! first registered your self!')
    elif sender in users and reciver not in users:
        print(f'the reciver {reciver} is not registered with us!')
    elif sender in users and reciver in users:
        if sender not in sent:
            sent[sender] = {}
        if reciver not in sent[sender]:
            sent[sender][reciver] = []
        sent[sender][reciver].append(message)
        print(f'{sender}, your message is sent to {reciver}')


def recive(reciver,sender):
    if reciver not in users:
        print(f'{reciver} you are not registered with us!')
    elif reciver in users and sender not in users:
        print(f'the sender {sender} is not registered with us')
    elif reciver in users and sender in users:
        if sender in sent and reciver in sent:
            message = sent[sender][reciver]
            print(f' all the message to {reciver} from sender {sender} are: \n {message}')

people('mohit',14,0)
people('riya',14,1)
# profile('mohit','age')
# profile('mohit','number')
# profile('mohit')
# print(users)
send('mohit','riya','good')
# print(sent)
send('riya','mohit','bye')
# print(sent)
send('mohit','riya','bye')
# print(sent)
recive('riya','mohit')