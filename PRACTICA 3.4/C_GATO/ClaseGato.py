#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRACTICA_3.4_PRACTICANDO CLASES Y OBJETOS
class Gato:
    especie="mamifero"

    def _init_(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        self.alimentos=[]

    def verEtapaDeVida(self):
        if self.edad>1:
            print(self.nombre, "es adulto")
        else:
            print(self.nombre, "es cachorro")

    def esAlimentoFavorito(self,alimento):
        return alimento in self.alimentos
