import random
x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
z = input("enter your choice:'a' to add 'b' to subtract 'c' to multiply 'd' to divide 'e' to find the square ")
if (z == "a"):
    sum = x+y
    print(sum)
elif (z == "b"):
    sub = x-y
    print(sub)
elif (z == "c"):
    product = x*y
    print(product)
elif (z == "d"):
    dividend = x/y
    print(dividend)
else:
    power = x**y
    print(power)
