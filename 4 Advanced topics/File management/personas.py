from io import open

# lectura y y guarda informacion del archivo personas.txt en variable contenido
txtfile = open('12-Ficheros\personas.txt', 'r', encoding='utf8')
contenido = txtfile.readlines()
txtfile.close()

personas = []

# recorre el contenido y lo agrega a lista personas como diccionario
for linea in contenido:
    arreglo = (linea.replace("\n","").split(';'))       # convierte el contenido en un arreglo, quita el salto de linea "\n" y separa por cada ";"
    personas.append( { "id": arreglo[0], "nombre": arreglo[1], "apellido": arreglo[2], "dob": arreglo[3] } )

for persona in personas:
    print("ID: {} - Nombre: {} {} - Fecha de nacimiento: {}".format(persona['id'],persona['nombre'],persona['apellido'],persona['dob']))