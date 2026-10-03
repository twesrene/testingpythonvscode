import random
import time

a = random.randint(1,20)
print("Wait computer is thinking about a number...")
time.sleep(1)
print("Computer is done!")

tries = 0
maxtries = 3

while tries <= maxtries :
    comp = (int(input("Please guess what number did the computer think, you got only 3 tries! ")))
    tries += 1

    if comp == a:
        print("Congrats you got the secret code!")
        break

    elif comp > a:
        print("The secret number is lower")

    elif comp < a:
        print("The secret number is higher")

    print ("You already tried",tries,"times")

    if tries == maxtries :
        print("Oh no! No more tries. The secret number is",a)
        break
