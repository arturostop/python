# During a project planning a list of task has been maked. For each of these tasks and order of priority has been assigned
# The lower the order number, the higher priority

from collections import deque

tasks = [ 
    [6, 'Distribution'],
    [2, 'Design'],
    [1, 'Conception'],
    [7, 'Maintenance'],
    [4, 'Production'],
    [3, 'Planning'],
    [5, 'Test']
]

print("== Disorderly tasks ==")
for task in tasks:
    print(task[0], task[1])

print("== Ordered tasks ==")

tasks.sort()   # ordering task list
cola = deque()  # blank queue

for t in tasks:      #for every task (t) on task list
    cola.append(t[1])   #add second index of tasks to queue

for t in cola:
    print(t)