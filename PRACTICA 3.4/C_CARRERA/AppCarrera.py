#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRACTICA_3.4_PRACTICANDO CLASES Y OBJETOS

from claseCarrera import *
from claseMateria import *

ing=Carrera("Ingeniería")
algebra=Materia("Algebra", "Ricardo Quinteros", 2010)
fisica=Materia("Fisica", "Margarita Gomez", 2006)
quimica=Materia("Quimica", "Lorenza Rios", 2003)
ing.agregarMateria(algebra,1234)

print(algebra.fechaInicioDictado)
print(fisica.fechaInicioDictado)
print(quimica.fechaInicioDictado)
