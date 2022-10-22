# The following program should follow the next instructions
# Save the magic_number = 2345679 (without 8)
# Read user_number, specify should be between 1 and 9 (make sure is a number)
# Multiply user_number 9 times
# Multiply magic_number and user_number
#Finally print magic_number

magic_number = 12345679
user_number = int(input("Escribe un número del 1 al 9: "))
user_number *= 9
magic_number *= user_number
print("El Número mágico es: ",magic_number)