#Prints out odd or even numbers
x = str(input("odd/even = "))
if x == 'even':
    for i in range(2,11,2):
        print(i)
elif x == "odd":
    for i in range(1,11,2):
        print(i)