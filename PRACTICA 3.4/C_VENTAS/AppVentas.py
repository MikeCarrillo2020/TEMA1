#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRACTICA_3.4_PRACTICANDO CLASES Y OBJETOS
from claseEmpleado import *
from claseAgenteVentas import *
from claseTripulante import *
from claseGerente import *

fernando = Empleado("Fernando", 35, "B110", 2000)
print(fernando.nombre)
print(fernando.calcularSueldo(1000,500))

mauricio = Tripulante("Mauricio", 25, "A110", 1000)
print(mauricio.mostrarRenovacionLicencia())

mariana = Gerente("Mariana", 45, "Z210", 200000)
print(mariana.calcularSueldo(100,6000))
