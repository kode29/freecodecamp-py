import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    password_length = int(input("Password Length: "))
    
    random.shuffle(characters)
    
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    # double-shuffle
    
    password = "".join(password)
    
    print(password)
    
option = input("Do you want to generate a password? [Y/n] ")
if option == "Y":
    generate_password()
elif option == "n":
    print("Goodbye")
    quit()
else:
    print("Invaild option")
    quit()