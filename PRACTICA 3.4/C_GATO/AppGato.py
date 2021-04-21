#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRACTICA_3.4_PRACTICANDO CLASES Y OBJETOS
from claseGato import *

a = Gato("Manchas", 3)
b = Gato("Lucifer", 1)

a.alimentos=["leche", "galletas", "pescado"]
b.alimentos=["leche", "croquetas", "pescado"]

print("El nombre del primer gato: ", a.nombre)
print("El nombre del segundo gato: ", b.nombre)
print("Edad del primer gato: ", a.edad)
a.verEtapaDeVida()
print("Edad del segundo gato: ", b.edad)
b.verEtapaDeVida()

print(a.esAlimentoFavorito("leche"))
print(b.esAlimentoFavorito("galletas"))
