# Function trim_range() receives 3 positive values:
# Minimum, maximum and x
# If x less than minimum, show minimum
# If x greather than maximum, show maximum
# If x is in the range between min and max show x as is

def trim_range(x,min,max):
    if x >= min and x <= max:
        print("Result: ",x)
    elif x < min:
        print("Result: ",min)
    elif x > max:
        print("Result: ",max)

print("Type values of the range and X")
min = input("Minimum: ")
max = input("Maximum: ")
x = input("X: ")

trim_range(x,min,max)