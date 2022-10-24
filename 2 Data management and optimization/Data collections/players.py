from traceback import print_tb


print("Configure every character class. The basic statistic is 2. Complete the following instructions.")
print("Knight has twice of life of a warrior")
print("The warrior has twice the attack and range of a knight")
print("Archer has the same health and attack as a warrior, but half their defense and twice their range")
print("The properties of the trhee characters are: \n")

knight = { 'life':2, 'attack':2, 'defense': 2, 'range':2 }
warrior  = { 'life':2, 'attack':2, 'defense': 2, 'range':2 }
archer   = { 'life':2, 'attack':2, 'defense': 2, 'range':2 }

print("Original values")
print('knight:\t',knight)
print('warrior:\t',warrior)
print('archer:\t',archer)


# Values
print("Configured values \n")
knight['life'] = warrior['life']*2
knight['defense'] = warrior['defense']*2

warrior['attack'] = knight['attack']*2
warrior['range'] = knight['range']*2

archer['life'] = warrior['life']
archer['attack'] = warrior['attack']
archer['defense'] = warrior['defense']/2
archer['range'] = warrior['range']*2

print('knight:\t',knight)
print('warrior:\t',warrior)
print('archer:\t',archer)