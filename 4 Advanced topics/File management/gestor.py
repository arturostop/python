from io import open
import pickle

class Personaje:
    
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
        #print('Se ha creado el personaje: {}'.format(self.nombre))
        
    def __str__(self):
        return '{} -> Vida: {} - Ataque: {} - Defensa: {} - Alcance: {}'.format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)
    
class Gestor:
    
    personajes = []  # Esta lista contendrá objetos de la clase Personaje
    
    def __init__(self):
        self.cargar()
        
    def agregar(self, p):
        for pTemp in self.personajes:
            if pTemp.nombre == p.nombre:
                print("El personaje {} ya está en el listado".format(pTemp.nombre))
                return
        self.personajes.append(p)
        print("{} Creado".format(p.nombre))
        self.guardar()

    def borrar(self, nombre):
        for pTemp in self.personajes:
            if pTemp.nombre == nombre:
                self.personajes.remove(pTemp)
                self.guardar()
                print("{} eliminado".format(nombre))
                return     

    def mostrar(self):
        if len(self.personajes) == 0:
            print("El listado de personajes está en blanco")
            return
        for p in self.personajes:
            print(p)  # Print toma por defecto str(p)
    
    def cargar(self):
        # Abre/Crea el archivo binario .pckl modo append binario y posiciona el puntero al inicio con seek(0)
        pcklfile = open('personajes.pckl', 'ab+')
        pcklfile.seek(0)
        try:
            self.personajes = pickle.load(pcklfile)
        except:
            pass
        finally:
            pcklfile.close()
            print("Se cargaron {} personajes".format( len(self.personajes) ) )
    
    def guardar(self):
        pcklfile = open('personajes.pckl','wb')
        pickle.dump(self.personajes, pcklfile)
        pcklfile.close()





G = Gestor()

G.agregar( Personaje("Caballero",4,2,4,2) )
G.agregar( Personaje("Guerrero",2,4,2,4) )
G.agregar( Personaje("Arquero",2,4,1,8) )

G.mostrar()

G.borrar("Arquero")

G.mostrar()