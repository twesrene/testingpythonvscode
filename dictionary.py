dict = {
    "A": "(你好) Ni Hao means Hello",
    "B": "(我们) Wo Men means Us",
    "C": "(五二零) Wu Er Ling/520 means I love you",
    "D": "(他们) Ta Men means Them",
    "E": "(我爱你) Wo Ai Ni means I love you"
            }

while True:
    print("These are the words available in the dictionary")
    print("A. 你好")
    print("B. 我们")
    print("C. 520")
    print("D. 他们")
    print("E. 我爱你")
    word = input("Please type in the words you dont know: ").upper()
    
    if word in dict.keys():
        print(dict[word])
        break
    else:
        print("invalid word")
    
