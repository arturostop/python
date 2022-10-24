# Table.py should satisfy the followings tasks:
# Read two args, both interger numbers > 0 from 1 to 9, or else show a error message
# First arg refers to rows in the table, second to columns
# If not args recieved, shows instructions about how to use the script
# The script will contain a for loop that iterates the number of times of the first argument
# Inside for loop, add a second for thats iterates the number of times of the second argument
# Inside second for run the instruction ** print("*",end=") **, (end=" evoid line break)
# Run the script and watch the reslut

import sys
if len(sys.argv) == 4:
    rows = int(sys.argv[1])
    columns = int(sys.argv[2])
    diagonal = sys.argv[3]

    if rows < 1 or rows > 9 or columns < 1 or columns > 9:
        print("Error. Adding arguments")
        print("Example. >python table.py [1 - 9] [1 - 9] 'diagonal number'")
    else:
        for r in range(rows):
            print("\n")
            for c in range(columns):
                if( r == c):
                    print(diagonal , "\t", end='')
                else:
                    print("*\t", end='')
                
else:
    print("Error. Add arguments")
    print("Example. >python table.py [1 - 9] [1 - 9] 'diagonal number'")