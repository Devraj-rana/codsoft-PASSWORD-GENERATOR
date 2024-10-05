import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def password_generator():
    try:
        length = int(input("Enter the desired password length: "))
        
        if length < 4:
            print("Password length should be at least 4 characters for better security.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    
    except ValueError:
        print("Error! Please enter a valid number.")

password_generator()
