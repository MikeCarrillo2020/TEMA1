#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRACTICA_3.4_PRACTICANDO CLASES Y OBJETOS
from claseCarrera import *

class Materia:
    def _init_(self, nombre, profesor, fecha):
        self.nombre=nombre
        self.profesor=profesor
        self.fechaInicioDictado=fecha

    @property
    def fechaInicioDictado(self):
        return self._fechaInicioDictado

    @fechaInicioDictado.setter
    def fechaInicioDictado(self, fecha):
        if fecha<2006:
            self._fechaInicioDictado=2006
        else:
            self._fechaInicioDictado=fecha
