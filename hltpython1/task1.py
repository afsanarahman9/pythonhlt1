import random
myName = input("hello! what is your name")
number = random.randint(1,10)
print("well" + myName + "i am thinkingof a number between 1 and 10")
guess = int(input("take a guess"))
if guess == number:
    print("good job," + myName + "you guessed the number")
else :
    print("wrong,better luck next time")    