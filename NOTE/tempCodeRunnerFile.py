cars = ["BMW", "Tesla", "Toyota","Audi"]
for i in range(len(cars)):
    if cars[i].startswith("T"):
        cars.pop(i) 
print(cars)   