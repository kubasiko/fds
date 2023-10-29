while True:
    password = input("введите пароль:")
    if len(password) < 8:
        print("короткий")
    elif '123' in password:
        print("простой")
    else:
        print("ОК")
        break
        