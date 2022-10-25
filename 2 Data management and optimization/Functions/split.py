# The function split() recieve a list and return two ordered lists
# First list only with even numbers
# The second list contains all odd numbers

def split(*args):
    numbers = []
    even = []
    odd = []

    for arg in args:
        numbers.append(arg)
        numbers.sort()
        if arg % 2 == 0:
            even.append(arg)
            even.sort()
        else:
            odd.append(arg)
            odd.sort()
    
    print( "Original list ",numbers )
    print( "Even: ",even )
    print( "Odd: ",odd )

split(-12, 84, 13, 20, -33, 101, 9)

# Second option with a list variable
print("\n")

def split_2 (list):
    list.sort()
    even = []
    odd = []

    for n in list:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    
    print("Original: ",list)
    print("Even ",even)
    print("Odd ",odd)

split_2([6,5,2,1,7])