# Read the radio of a circle and find the area
# Using pi= 3.1514... or import math module

import math
import sys

def area_circle(r):
    return math.pi*(r**2)

if len(sys.argv) == 2:
    r = int( sys.argv[1] )

    if r < 1:
        print("Radio should be greather than 0")
        print("'>python circle.py [radio]'")
    else:
        print("Circle info. \n Radio: ",r)
        print(" Area: ",area_circle(r))

else:
    print("Add arguments \n '>python circle.py [radio]'")