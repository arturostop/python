# Create a function "modify()" that from a list of numbers make the following tasks whitout modify the original:
# Delete all duplictes
# Sort list from largest to smallest
# Delete odd numbers
# Sum all numbers left in the list
# Add as a first element of the list the result of the sum
# Show the modified list
# Finally, after call the function, test that the sum of all numbers starting from the second, match with the first number of the list

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modify(l):              #define function that recieve a list
    l = list(set(l))        #set() create a set and delete duplicate and list() to save the result on a list
    l.sort(reverse=True)    #sort() with parameter reverse=True order a list from largest to smallest

    l_tmp = []              #temporal list contains only pairs numbers
    for n in l:
        if n%2 == 0:
            l_tmp.append(n)

    suma = sum(l_tmp)
    l_tmp.insert(0,suma)
    
    return l_tmp


new_list = modify(lista)

print("Sum all numbers starting form de second: ", sum(new_list[1:]))
print(new_list[0] == sum(new_list[1:]))
print(new_list)
print(lista)