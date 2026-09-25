import time
import random

skorsaya = 0
skorcomp = 0

while True:

    print("1 = rock , 2 = paper , 3 = scissor")
    x = int(input("What number are you picking?(1,2,3)"))
    y=random.randint(1,3)
    print("The computer picks",y)
    
    if y == x :
        print("Wait its processing...")
        time.sleep(1)
        print("Its a tie")
        print("Your score is",skorsaya," and The Computer score is",skorcomp)

    elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
        print("Wait its processing...")
        time.sleep(1)
        print("You have won")
        skorsaya += 1
        print("Your score is",skorsaya ," and The Computer score is",skorcomp)

    elif (x == 3 and y == 1) or (x == 1 and y == 2) or (x == 2 and y == 3) :
        print("Wait its processing...")
        time.sleep(1)
        print("You have lost")
        skorcomp += 1
        print("Your score is",skorsaya," and The Computer score is",skorcomp)

    else:
        print("Error your number is not listed here...")
        time.sleep(1)
        print("Your Final Score is",skorsaya,"and the Computer score is",skorcomp)
        break
