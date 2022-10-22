# Ask the user for a number, an chek out if exist on a given list

list = [1, 3, 6, 9]

while True:
    number = int(input("Type a number between 0 and 9: "))
    if number >= 0 and number <= 9:
        break
if number in list:
    print("Ok, you can find the number ", number," on the list: ",list)
else:
    print("Nope, the number ", number," is not on the list: ",list)