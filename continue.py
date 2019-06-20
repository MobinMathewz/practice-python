#prints out 1 to 100 skipping divisibles of 3 and 5

for i in range(1,101):   
    if i % 3 == 0 and i % 5==0:
        continue
    print(i)

print("Bye")
