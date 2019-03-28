MIN_LENGTH = 3


def main():
    password = get_password()

    while len(password) < MIN_LENGTH:
        password = get_password()
    print(len(password) * '*')


def get_password():
    password = input("Password: ")
    return password


main()
