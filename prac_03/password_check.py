
MIN_LENGTH = 3

password = input("Password: ")

while MIN_LENGTH >= 0:
    if len(password) >= MIN_LENGTH:
        print(len(password) * '*')
    password = input("Password: ")

