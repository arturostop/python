from io import open
import sys

txtfile = open('contador.txt', 'a+')
txtfile.seek(0)
contenido = txtfile.readline()

if len(contenido) == 0:
    contenido = '0'
    txtfile.write(contenido)

txtfile.close()

try:
    contador = int(contenido)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'inc':
            contador += 1
        elif sys.argv[1] == 'dec':
            contador -= 1
        else:
            print("Escribe como argumento 'inc' para incrementar el contador o 'dec' para disminuirlo")
    
    txtfile = open('contador.txt', 'w')
    txtfile.write( str(contador) )
    txtfile.close
    
    print("Visitas =",contador)
    
except:
    print("Error: Archivo dañado X.X")