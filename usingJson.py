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
    
    if option == 1:
        information = {}

        try:
            # Trying to load the file .json
            with open('database.json', 'r') as fileDatabase:
                dictionary = json.load(fileDatabase)
        except:
            # If file doesn't exist, create a new dictionary
            dictionary = {}

        user = input('\nType an username: ')
        password = getpass.getpass('Type your password: ').encode('utf-8')

        salt = bcrypt.gensalt() # Generating a random salt
        hash_password = bcrypt.hashpw(password, salt) # Creating a password hash

        age = int(input('Type your age: '))
        print('\n')

        # Putting all the information on dictionary
        information = {
            "password": hash_password.decode('utf-8'), # I needed to use decode() because a json file doesn't accept bytes objects
            "age": age
        }
        dictionary[user] = information

        try:
            with open('database.json', 'w') as fileDatabase:
                json.dump(dictionary, fileDatabase, indent=4)
        except Exception as e:
            print(f'Fail to write on on file: {e}')
            exit()
