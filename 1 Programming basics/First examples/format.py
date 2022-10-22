# Exercise 4
# Fxix the next string with the format "Name" "LastName" has got a "note" grade

print("Original string: zeréP nauJ,01")

string = "zeréP nauJ,01"

fixString = string[::-1]
print(fixString)
print(fixString[3:] + " has got a " + fixString[:2] + " grade")