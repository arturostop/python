# Read two numbers and select betwieen the 3 option menu
# 1-. Show the sum of the two numbers
# 2.- Substract the first minus the second
# 3.- Show the product of both numbers
# In case of a no valid option, the program inform the user

n1 = int(input("First number: "))
n2 = int(input("Second number: "))

while(True):
    print("""Select one option: 
        1) Add
        2) Substract
        3) Multiply
        4) Select new numbers
        0) Exit
            """)
    n = input("Your selection: ")
    
    if n == '1':
        print("You chose add two numbers")
        print(n1," + ",n2," = ",n1+n2)
        
    elif n == '2':
        print("Your chose substract two numbers")
        print(n1," - ",n2," = ",n1-n2)
    
    elif n == '3':
        print("You chose multiply two numbers")
        print(n1," x ",n2," = ",n1*n2)
    
    elif n == '4':
        n1 = int(input("First number: "))
        n2 = int(input("Second number: "))
    
    elif n == '0':
        print("Bye")
        break
    else:
        print("Try again, you selection should be an option of the given menu")
    
    