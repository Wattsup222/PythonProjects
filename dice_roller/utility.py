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
