# Make a program that adds all the even numbers form 0 to 100

print(sum(range(0,101,2)))

# another option with loops
print("\n Option 2")
n = 0
suma = 0

while n <= 100:
    if n % 2 == 0:
        suma += n
    n += 1
print(suma)