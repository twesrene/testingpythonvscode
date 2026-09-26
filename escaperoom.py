import time

room = {
    "start": {"rooms": ["1"], "items":[]},
    "1": {"rooms": ["start", "2", "3"], "items":[]},
    "2": {"rooms": ["1"], "items":["key"]},
    "3": {"rooms": ["1", "4"], "items":[]},
    "4": {"rooms": ["3", "5"], "items": []},
    "5": {"rooms": ["4", "Escape"], "items":[]}
}

ruangan = "start"
key = False

while True:
    print("============================")
    print("You are in a room", ruangan)
    
    for near_room in room[ruangan]["rooms"]:
        print("You can only enter these room", near_room)
        
    new_room = input("What room are you going to choose?")
    
    if near_room not in room[ruangan]["rooms"]:
        print("This room isnt available")
        time.sleep(1)
        continue
    
    if new_room == "Escape" and not key :
        print("You dont have any keys")
        time.sleep(1)
        continue
    
    if new_room == "Escape" :
        print("You win!")
        time.sleep(2)
        break
    
    ruangan = new_room
    if "key" in room[ruangan]["items"]:
        key = True
        print("You have obtained a key")
        room[ruangan]["items"].remove("key")
        time.sleep(1)
