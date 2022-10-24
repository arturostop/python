# Make a program who follows the next instructions:
# Create a set named users with users Marta, David, Elvira, Juan and Marcos
# Create a set named admins with admins Juan and Martha
# Delete admin Juan from admins set
# Add Marcos as a new admin, but he is still in users set
# Show all users in screen dinamically, also show if each user are an administrator or not.

users = {'Marta','David','Elvira','Juan','Marcos'}
admins = {'Juan','Marta'}

print("Users:",users)
print('Admins set before edit',admins)

admins.discard('Juan')
admins.add('Marcos')

for u in users:
    if u in admins:
        print(u,"is admin")
    else:
        print(u,"not admin")
        
print('Users final set:',users)
print('Admins final set:',admins)