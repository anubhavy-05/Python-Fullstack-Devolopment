x=int(input("enter the number:"))
if x>5000:
    print("good time to sell")
elif x>=3000 and x<=5000:
    print("Average price,you can hold ")
elif  x<3000: 
    print("market is down, hold the crop")
else:
    print("invalid price")