x=[]
if x == False:
    print("Btsman") # This will not be printed because an empty list is not equal to False.
elif x is False:
        print("Iron man") # This will not be printed because an empty list is not the same object as False.
elif not x:
        print("Spiderman") # Output: "Spiderman" (since an empty list is considered False in a boolean context, the not operator will evaluate to True and "Spiderman  " will be printed)
else:
        print("Superman")  