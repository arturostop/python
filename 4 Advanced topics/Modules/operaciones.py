def suma(a, b):
    try:
        ans = a + b
    except TypeError:
        print("No se puede sumar letras y numeros")
    else:
        return ans

def resta(a, b):
    try:
        ans = a - b
    except TypeError:
        print("No se puede restar letras y numeros")
    else:
        return ans

def multiplicacion(a, b):
    try:
        ans = a * b
    except TypeError:
        print("No se puede multiplicar letras y numeros")
    else:
        return ans

def division(a, b):
    try:
        ans = a / b
    except TypeError:
        print("No se puede dividir letras y numeros")
    except ZeroDivisionError:
        print("Imposible dividir entre cero")
    else:
        return ans
