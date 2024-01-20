import random
import string

def gen():
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(4))

number = 100

usernames = [gen() for _ in range(number)]

with open("users.txt", "w") as users_file:
    for username in usernames:
        users_file.write(f"{username}\n")