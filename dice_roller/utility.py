from random import choice


def generate_name():
    file = open("names.txt", 'r')
    read = file.readlines()
    names = []
    for line in read:
        names.append(line.strip())
    file.close()
    return choice(names)


def create_username():
    while True:
        username = input("Input a username: ")
        if 2 < len(username) <= 20:
            if username.isalnum():
                return username
            else:
                print("Username must only contain letters and numbers")
        else:
            print("Username must be between 3 and 20 characters")
