# Find the error, create an an exeption and explain the reason
try:
    division = 10/0
except:
    print("Error: Zero division")

# Find the error, create an an exeption and explain the reason
try:
    list = [1, 2, 3, 4, 5]
    list[10]
except:
    print("The list length is ",len(list),"try again with that limit")

try:
    colors = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    colors['blanco']
except:
    print("ID doesn't exist")

try:
    result = 15 + "20"
except TypeError:
    print("An int and string cannot be added")

