def f1():
    print("enter a number") # this function simply prints a message when called.
    n=int(input()) # it takes an input from the user and converts it to an integer.
    for e in range(1,n+1):
        print(e**2,end=" ") # it prints all the numbers from 0 to n-1 (inclusive) using a for loop.
        print() # it prints a new line after the loop is finished.
f1() # the function is called to execute the code inside it.
f1()