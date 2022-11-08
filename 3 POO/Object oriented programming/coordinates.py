# Make a class named dot with two coordinates X and Y
# Add a constructor to crate corrdinates easily. If not values are recieved the value will be 0
# Overwrite string method, to print the coordinates in the format (X,Y)
# Add a method named quadrant, who detects in wich quadrant the point is
# Add a method named vector, this will take another point and calulate the result vector of this two points
# Add a method named distance, this will take another point and calculate the distance between this two points and print on screen.

# Add a class named rectanvle with two points (initial and final), who represent the triangle diagonal
# Add a constructor method to create both points easily,if the data is not recieved these points are at the origin by defalut
# Add to the rectangle a method named base who show this data
# Add to the rectangle a method named height who show this data
# Add to the rectangle a method named area who show this data

import math

class Dot:
    # constructor to create point x,y
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        #print("Point ({},{}) created".format(x,y))

    # overwrite string method
    def __str__(self):
        return "({},{})".format(self.x,self.y)

    # Method to detect the quadrant
    def quadrant(self):
        if self.x > 0 and self.y > 0:
            print("Point {} is on quadrant 1".format(self))
        elif self.x < 0 and self.y > 0:
            print("Point {} is on quadrant 2".format(self))
        elif self.x > 0 and self.y < 0:
            print("Point {} is on quadrant 3".format(self))
        elif self.x < 0 and self.y < 0:
            print("Point {} is on quadrant 4".format(self))
        else:
            print("Point {} on the origin".format(self))
    
    # Method to create point x2,y2, and the resulting vector regarding x,y
    def vector(self,p):
        print("The resulting vector between {} and {} is ({},{})".format(self,p, p.x - self.x, p.y - self.y))
    
    def distance(self,p):
        d = math.sqrt( (p.x-self.x)**2 + (p.y - self.y)**2 )
        print("Distance from {} to {} is {}".format(self,p,d))


#constructor to create point x,y
class Rectangle:
    def __init__(self, pInicial=Dot(), pFinal=Dot()):
        self.pInicial = pInicial
        self.pFinal = pFinal
    
    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        print("Rectangle base: {}".format(self.base))

    def height(self):
        self.height = abs(self.pFinal.x - self.pInicial.y)
        print("Rectangle height: {}".format(self.height))

    def area(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        self.height = abs(self.pFinal.y - self.pInicial.y)
        self.area = self.base * self.height
        print("Rectangle area: {}".format(self.area))


a = Dot(2,3)
b = Dot(5,5)
c = Dot(-3,-1)
d = Dot()

a.quadrant()
c.quadrant()
d.quadrant()

a.vector(b)
b.vector(c)

a.distance(d)
b.distance(a)

a.distance(d)
b.distance(d)
c.distance(Dot(0,0))

r = Rectangle(a,b)
r.base()
r.height()
r.area()