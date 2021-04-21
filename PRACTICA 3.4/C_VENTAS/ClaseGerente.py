#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRACTICA_3.4_PRACTICANDO CLASES Y OBJETOS
from claseEmpleado import *
from claseAgenteVentas import *

class Gerente(Empleado):
    def calcularSueldo(self, descuentos, bonificaciones):
        return self.sueldoBase-descuentos+bonificaciones
