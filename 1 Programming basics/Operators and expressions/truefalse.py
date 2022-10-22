# Exercise 1
# Read two numbers and determine following aspects:
# - If two numbers are equal
# - If two numbers are different
# - If first number are greater than second
# - If second number is greater or equal than first

n1 = int(input("First number: "))
n2 = int(input("Second number: "))

print("Both numbers are equal: ", n1 == n2)
print("Both numbers are different: ", n1 != n2)
print("First number are greater: ", n1 > n2)
print("Second number are greater or equal than the first: ", n2 >= n1)