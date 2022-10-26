# Make a function add_once() that recieves a list and an element.
# Function should add the new element at the end of the list but only if not exist
# If the element is allready in the list, use a ValueError and show the error message

list = [1, 5, -2]

def add_once(list,el):
    try:
        if el in list:
            raise ValueError
        else:
            list.append(el)
    except ValueError:
        print("Error: Cannot add duplicate elements => {}".format(el))

print("Original list: ", list)

while(True):
    print("""Select an option: 
    1) Add a number
    2) Add an string
    0) Exit
    """)
    option = input("Option: ")

    if option == '1':
        element = int( input("Add element: ") )
        add_once(list,element)
        print(list)

    if option == '2':
        element = input("Add element: ")
        add_once(list,element)
        print(list)
    
    elif option == '0':
        print("Final list: ",list)
        print("Bye")
        break
    else:
        print("Try again, you selection should be an option of the given menu")