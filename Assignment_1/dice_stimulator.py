import random
while True:
    val = int(input("Press 1 to continue dice rolling stimulator and 2 to stop "))
    print (val)
    if val == 1:
        r = random.randint(1,6)
        if(r == 1):
            print(f"Dice rolled to {r}")
        elif(r == 2):
            print(f"Dice rolled to {r}")
        elif(r == 3):
            print(f"Dice rolled to {r}")
        elif(r == 4):
            print(f"Dice rolled to {r}")
        elif(r == 5):
            print(f"Dice rolled to {r}")
        elif(r == 6):
            print(f"Dice rolled to {r}")
    elif val == 2:
        break
