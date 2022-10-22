# Exercise 3
# The following matrix (or a list with nested lists) should satisfy the next condition:
# Every fourth element of each row needs to be the result of add the first three numbers
# Example: [1,2,3,6]

matriz = [ 
    [1, 1, 1, 16],
    [2, 2, 2, 15],
    [3, 3, 3, 14],
    [4, 4, 4, 13]
]

matriz[0][-1] = sum( matriz[0][:-1] )
matriz[1][-1] = sum( matriz[1][:-1] )
matriz[2][-1] = sum( matriz[2][:-1] )
matriz[-1][-1] = sum( matriz[-1][:-1] )


print(matriz)