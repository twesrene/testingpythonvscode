import time
import random

p1 = {"name": "Chris", "hp": 100, "power": 10}
p2 = {"name": "Axel", "hp": 100, "power": 10}

while True:
    atk1 = random.randint(1, 10)
    print(p1["name"], "attacked", p2["name"], "using", p1["power"]+atk1,"power")
    p2["hp"] -= p1["power"] + atk1 
    time.sleep(1)

    atk2 = random.randint(1, 10)
    print(p2["name"], "attacked", p1["name"], "using", p2["power"]+atk2,"power")
    p1["hp"] -= p2["power"] + atk2
    time.sleep(1)

    print(p1["name"], p1["hp"])
    print(p2["name"], p2["hp"])
    
    if p1["hp"] <= 0  :
        print("The Winner is Axel")
        break
    elif p2["hp"] <= 0 :
        print("The Winner is Chris")
        break
    
    time.sleep(1)
