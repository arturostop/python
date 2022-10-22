# Exercice 1
# Print average of three static numbers

n1 = 9
n2 = 3
n3 = 6

print("Average of: ", n1, " ", n2, " ", n3)

media = (n1 + n2 + n3) / 3
print("Average: ", media)

# Exercise 2
# Following the last example, assuming that each number is a class note, and we want to know the average.
# the thing is, each note has a porcentage value

print("\n")
print("With a porcentage value for each note, find the avg of the final score")
print("First grade, 15%")
print("First grade, 35%")
print("First grade, 50%")

note1 = 10
note2 = 7
note3 = 4
print("\n Note 1: ",note1, "\n", "Note 2: ",note2, "\n", "Note 3: ",note3)

avg = note1 * 0.15 + note2 * 0.35 + note3 * 0.50
print("The average score is: ",avg)