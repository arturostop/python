# Create one object at least of every subclasss and add them to a list named vehicles
# Make a catalog() that receive  a list of vehicles read it and show the name of his class and his attributes
# Modify catalog() function to get an optional argument wheels, filtering by the number of wheels in the argument. Also
# it has to show "I find {} vehicles with {} wheels:" only if the argument is sent. Test with 0, 2 and 4 wheels as an argument.


class Vehicle():
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return "Color {}, {} wheels".format( self.color, self.wheels )

class Car(Vehicle):
    def __init__(self, color, wheels, speed, cylinder):
        super().__init__(color, wheels) #use super() whitout self instead of vehicle
        self.speed = speed
        self.cylinder = cylinder

    def __str__(self):
        return super().__str__() + ", {} kn/k, {} cylinder".format(self.speed, self.cylinder)


class Van(Car):
    def __init__(self, color, wheels, speed, cylinder, load):
        super().__init__(color, wheels, speed, cylinder)
        self.load = load
    
    def __str__(self):
        return super().__str__() + ", {} kg capacity".format(self.load)

class Bike(Vehicle):
    def __init__(self, color, wheels, type):
        super().__init__(color, wheels)
        self.type = type

    def __str__(self):
        return super().__str__() + ", type: {}".format(self.type)

class Motorcycle(Bike):
    def __init__(self, color, wheels, type, speed, cylinder):
        super().__init__(color, wheels, type)
        self.speed = speed
        self.cylinder = cylinder

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.speed, self.cylinder)


vehicles = [
    Car("Blue",4,180,8),
    Van("White",4,150,10,200),
    Bike("Black",2,"Mountain"),
    Motorcycle("Green",2,"Sport",200,4)
]


def catalog(list, wheels=None):
    if wheels != None:
        c = 0
        for v in vehicles:
            if v.wheels == wheels:
                c += 1
    print("I find {} vehicles with {} wheels".format(c, wheels))
    print("===========================================================") # edit to show wheels in argument

    for v in list:
        if wheels == None:
            print("{} {}".format( type(v).__name__, v ))
        else:
            if v.wheels == wheels:
                print("{} {}".format(type(v).__name__, v))

catalog(vehicles,2)