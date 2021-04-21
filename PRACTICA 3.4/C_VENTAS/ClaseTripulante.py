#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRACTICA_3.4_PRACTICANDO CLASES Y OBJETOS
from claseEmpleado import *
from claseAgenteVentas import *
from claseGerente import *

class Tripulante(Empleado):
    def mostrarRenovacionLicencia(self):
        if self.edad<50:
            print("Renueva su licencia cada 1 año")
        else:
            print("Renueva su licencia cada 6 meses")
