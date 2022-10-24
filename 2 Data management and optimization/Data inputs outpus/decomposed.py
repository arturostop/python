# This program read a positive interger number
# If not, show instructions about how to use the script
# This script goal is decompose the number in units, tens, hundreds, thousands...
# Example:
# >python decomposed.py 3647
# > 0007
#   0040
#   0600
#   3000

import sys
if len(sys.argv) == 2:
    num = int(sys.argv[1])   #read a number as an argument

    if num < 1 or num > 9999:
        print("Error. Add arguments correctly")
        print("Example: >python decomposed.py [1 - 9999] [1 - 9999]")
    else:
        cadena = str(num)       #convert from int to string. 
        longitud = len(cadena)  #Length of the converted string for the array

        for i in range(longitud):
            print( "{:04d}".format( int( cadena[longitud-1-i] )*10 **i ) )

else:
    print("Error. Add arguments correctly")
    print("Example: >python decomposed.py [1 - 9999] [1 - 9999]")
