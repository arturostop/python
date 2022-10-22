# Ask the user hoy many numbers wants to consider in the program
# Read all the numbers and show the average

suma = 0
n = int(input("How many numbers you want to consider? "))

#numeros = list(range(n))

for i in range(n):

    suma += float(input("Value: "))

media = suma /n

print(n)
print(suma)
print(media)
print("We work with ",n," numbers, the summation is: ",suma," Average: ",media)