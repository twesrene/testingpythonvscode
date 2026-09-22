a = int(input("Insert your first number "))
b = int(input("Insert your second number "))
c = input("Insert the equations that you want (+,-,*,/) ")

if c == "+":
    print(a,"+",b,"=",a+b)

elif c == "-":
    print(a,"-",b,"=",a-b)

elif c == "*":
    print(a,"*",b,"=",a*b)

elif c == "/":
    print(a,"/",b,"=",a/b)

else:
    print("Sorry this equation isnt available.")
