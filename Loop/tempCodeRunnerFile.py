pass="python123"    
while True:
    password = input("enter the password:")
    if password == pass:
        print("correct password, welcome to the system")
        break
    else:
        print("wrong password, try again")
