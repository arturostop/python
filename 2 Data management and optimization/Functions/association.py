# Make a function who reads two numbers and compare them
# If first number is greather than the second, show 1
# If second number is greather than the first, show -1
# If both numbers are equal, show 0

def association (a,b):
    if a > b:
        print("Value A > B")
        return 1
    elif a < b:
        print("Value B > A")
        return -1
    #elif a == b:
    else:
        print("Value A = B")
        return 0

a = int( input("A: ") )
b = int( input("B: ") )

print ( "Result: ",association(a,b) )