#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRACTICA_3.4_PRACTICANDO CLASES Y OBJETOS
class Carrera:
    def _init_(self, nombre):
        self.nombre=nombre
        self.materias={}

    def agregarMateria(self, materia, codigo):
        self.materias[codigo]=materia
