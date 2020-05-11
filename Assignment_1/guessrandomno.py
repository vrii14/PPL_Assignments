import random
r = random.randint(1,100)
#print (r)
while True:
    n = int(input("Guess the random number generated"))
    if(n == r):
        print("You guessed the correct number")
        break
    else:
        if(n > r):
            print("The number is smaller than you guessed")
            continue
        elif(n < r):
            print("The number is greater than you guessed")
            continue

