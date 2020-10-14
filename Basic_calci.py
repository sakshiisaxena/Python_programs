print("--------------------------------------------BASIC CALCULATOR-------------------------------------------")
print("press 1 to ADD");
print("press 2 to SUBTRACT");
print("press 3 to MULTIPLY");
print("press 4 to DIVIDE");

choice = int(input())

if choice in (1,2,3,4):
    num1 = int(input("enter 1st number :"))
    num2 = int(input("enter 2nd number :"))
    if choice == 1:
        print("The sum is =", num1+num2)
    elif choice ==2:
        print("The subt is =", num1-num2)
    elif choice ==3:
        print("The product is =", num1*num2)
    else:
        print("The division is =", num1/num2)
    
    