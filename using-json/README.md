## Here I'll talk about the project and how to execute it.

1 - You'll need to install the bcrypt module that isn't a built-in Python module:
```bash
pip install bcrypt
```

2 - So, on the code we need to import three modules, that are:

```python
import bcrypt
import json
import getpass
```

> Let's talk about ```bcrypt``` first.
- We'll use this module to encrypt the passwrod using the method ```hashpw()```.
  - This method basically get the user password and call a hash function that encrypt the string.

>Now, the ```json``` module:
- Basically we use this module to store the data in a .json file.

>Finally, the ```getpass``` module:
- We use this module to hide the password that the user is typing; the method is called ```getpass```.

3 - Now, the function ```choose_feature()```:
- In this function, the user chooses an option, that are:
  - Register
    - Here the user can register a new person in the database.
    - The program asks for a name, password and age.
  - Login
    - In this option, the user type the name of a person and the program asks for a password, if the passwrod typed match with the one in the database, the program displays the person's age.
    - If the name isn't in the database an error message is displayed.
    - If the name exists and the password typed doesn't match with the database one, an error message is also displayed.
  - Close
    - This option simply finish the program.

4 - Finally, we have a loop that implements all the functions described previously.

#

## How to execute the program?

### Windows:
- First, you'll need to have Python version 3.11 installed on your PC.
- Than, you just need to execute the following command at the folder that contains the ```usingJson.py``` file:
  ```bash
  python usingJson.py
  ````