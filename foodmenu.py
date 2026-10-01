import time

ayam = 0
burger = 0
coke = 0

x = str
while x != 'Q':
    print("Please choose from our menu")
    print("A Chicken")
    print("B Burger")
    print("C Coke")
    print("Q Keluar")
    x = (input("Type the food code that you want ")).upper()

    if x == 'A': 
        A = int(input("How many chicken do you want? "))
        ayam += A
        time.sleep(1)
        print("You Order",A, "Chicken")
    elif x == 'B':
        B = int(input("How many burger do you want? "))
        burger += B
        time.sleep(1)
        print("You Order",B, "Burger")
    elif x == 'C': 
        C = int(input("How many coke do you want? "))
        coke += C
        time.sleep(1)
        print("You Order",C, "Coke")
    elif x == 'Q':
        print("Terima kasih")
        time.sleep(1)
        print("You have ordered",ayam, "chicken,",burger,"burger, and",coke,"Coke")
    else:
        print("Sorry we dont have this menu")
    
