#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRACTICA_3.4_PRACTICANDO CLASES Y OBJETOS
from claseEmpleado import *
from claseTripulante import *
from claseGerente import *

class AgenteVentas(Empleado):
    def _init_(self, nombre, edad, legajo, sueldo, mostrador):
        self.numeroMostrador=mostrador
        super()._init_(nombre, edad, legajo, sueldo)
