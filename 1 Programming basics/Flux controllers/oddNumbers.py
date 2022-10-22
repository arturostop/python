# Read a number
# It should be and odd number, if not ask for another number until the given number are correct

n = 0
while n % 2 == 0:
    n = int(input("Type an odd number: "))

print("Thank you")