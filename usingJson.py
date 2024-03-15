# Here I'll practice some basics data persistence with JSON and I'll use cryptography in some data.

import json
import bcrypt
import getpass

def choose_feature():
    print("[1] Register")
    print("[2] Login")
    print("[3] Close")
    
    return int(input('Type an option: '))

while True:
    option = choose_feature()
    dictionary = {}
    information = {}

    if option == 1:
        user = input('\nType an username: ')
        password = getpass.getpass('Type your password: ').encode('utf-8')

        salt = bcrypt.gensalt() # Generating a random salt
        hash_password = bcrypt.hashpw(password, salt) # Creating a password hash

        age = int(input('Type your age: '))
        print('\n')

        # Putting all the information on dictionary
        information['password'] = hash_password
        information['age'] = age
        dictionary[user] = information

        print(type(dictionary))

        json_string = json.dumps(dictionary)

        file = open('database.json', 'w')
        file.write(json_string)
