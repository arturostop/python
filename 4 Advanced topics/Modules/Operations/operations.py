def suma(a,b):
    try:
        r = a + b
    except TypeError:
        print("Data Type not valid")
    else:
        return r

def resta(a,b):
    try:
        r = a - b
    except TypeError:
        print("Data Type not valid")
    else:
        return r

def producto(a,b):
    try:
        r = a * b
    except TypeError:
        print("Data Type not valid")
    else:
        return r

def division(a,b):
    try:
        r = a / b
    except TypeError:
        print("Data Type not valid")
    except ZeroDivisionError:
        print("Error: Cannot be divided by zero")
    else:
        return r
