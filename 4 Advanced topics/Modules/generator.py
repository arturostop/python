import random
import math

def leer_numero(ini, fin, mensaje):

    while True:
        try:
            valor = int( input(mensaje) )
        except:
            print("Número no valido")
        else:
            if valor >= ini and valor <= fin:
                break
    return valor

def generador():
    numeros = leer_numero(1,20,"¿Cuántos numeros se necesitan? [1 - 20]: ")
    redondeo = leer_numero(1,3,"Redondear - [1]:hacia arriba [2]:hacia abajo [3]: normal: ")

    lista = []
    for i in range(numeros):
        numero = random.uniform(0, 101)
        if redondeo == 1:
            print("{} => {}".format(numero, math.ceil(numero)))
            numero = math.ceil(numero)

        elif redondeo == 2:
            print("{} => {}".format(numero, math.floor(numero)))
            numero = math.floor(numero)

        elif redondeo == 3:
            print("{} => {}".format(numero, round(numero)))
            numero = round(numero)
        
        lista.append(numero)
    
    return lista

generador()