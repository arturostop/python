# Given two list, generate a third one with all the duplicates from the first two
# but the third list should not have duplicates

l1 = ["h","o","l","a"," ","m","u","n","d","o"]
l2 = ["h","o","l","a"," ","l","u","n","a"]
l3 = []

for i in l1:
    if i in l2 and i not in l3:
        l3.append(i)


print(l1)
print(l2)
print(l3)