
def main():


    MIN_LENGTH = 3

    password = get_password()

    while MIN_LENGTH >= 0:
        if len(password) >= MIN_LENGTH:
            print(len(password) * '*')
        password = get_password()


def get_password():
    password = input("Password: ")
    return password


main()
