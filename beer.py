#Beer vending machine

needed = int(input("How many beer you want? "))
available = 5
i = 1
while i<=needed:
    print("Beer")
    i+=1
    if i>available:
        print("Out of stock")
        break
print("Bye")
