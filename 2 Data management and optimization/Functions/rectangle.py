# Find the rectangle area with a function

import sys

def area_rectangle(b,h):
    return b*h

if len(sys.argv) == 3:
    b = int( sys.argv[1] )
    h = int( sys.argv[2] )

    if b < 1 or h < 1:
        print("Add arguments '>python rectangle.py [base][height]'")
    else:
        print("Rectangle info. \n Base: ",b,"\n Height: ",h)
        print(" Area: ",area_rectangle(b,h),"m²")

else:
    print("Add arguments '>python rectangle.py [base][height]'")
