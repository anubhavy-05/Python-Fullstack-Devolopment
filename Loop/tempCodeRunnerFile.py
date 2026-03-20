sahi_password = "python123"
password = input("enter the password:")
while password != sahi_password:
    print("wrong password, try again")
    password = input("enter the password:")
print("correct password, welcome to the system")