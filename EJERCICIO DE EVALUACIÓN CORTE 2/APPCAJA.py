#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: EJERCICIO DE EVALUACIÓN

#Aquí importamos de nuestra clase que está en la misma ubicación que nuestra app

from ClaseCaja import *
#Aquí construimos el objeto de la claseCaja
cajas = Caja(20,20,30)
#Aquí usamos el método mostrar
print (cajas.mostrar())
#Aquí se muestra el volumen
print (cajas.calcularVolumen())
#Aquí se muestra el área total
print("AREA TOTAL: ",cajas.calcularAreaTotal())
#Aquí se crea el clon
miClon= cajas.clon()
#Aquí mostramos la información del clon
print("LAS CANTIDADES DE NUESTRO CLON EXACTAS DE LA PRIMERA CAJA: ", miClon.mostrar())
#Aquí creamos una caja más grande a partir del clon con ayuda de "cajas"
cajas25MasGrande = cajas.crearCajaGrande()
print(cajas25MasGrande.mostrar())
#Aquí verificamos si la primer caja cabe en la segunda
verificacion = miClon.cabe1DentroDe2(miClon,cajas25MasGrande)
print("LA CAJA ES MÁS GRANDE: ", verificacion)

