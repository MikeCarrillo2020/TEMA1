#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRÁCTICA 3.3 - PRACTICANDO FUNCIONES PYTHON
from random import randint


precio = 150
capacidad = 10000
monto = capacidad * precio
sumaRealDesc= 0
sumaPercibida= 0

clasificación = {"PRIMERA":0, "SEGUNDA":0, "TERCERA":0, "CUARTA":0, "QUINTA":0}
descuentos = {
    "1":(precio*0.30),
    "2":(precio*0.10),
    "3":(precio*0.15),
    "4":(precio*0.25),
    "5":(precio*0.35)
    }
suma_descuentos = [0, 0, 0, 0, 0]
suma_entradas = {"1":0, "2":0, "3":0, "4":0, "5":0}

for i in range(10000):
    edad = randint(5,120)
    if edad > 5 and edad <14:
        clasificación["PRIMERA"] +=1
        suma_descuentos[0] += descuentos["1"]
        suma_entradas["1"] += precio - descuentos["1"]
    elif edad > 15 and edad <19:
        clasificación["SEGUNDA"] +=1
        suma_descuentos[1] += descuentos["2"]
        suma_entradas["2"] += precio - descuentos["2"]
    elif edad > 20 and edad < 45:
        clasificación["TERCERA"] +=1
        suma_descuentos[2] += descuentos["3"]
        suma_entradas["3"] += precio - descuentos["3"]
    elif edad > 46 and edad <65:
        clasificación["CUARTA"] +=1
        suma_descuentos[3] += descuentos["4"]
        suma_entradas["4"] += precio - descuentos["4"]
    else:
        clasificación["QUINTA"] +=1
        suma_descuentos[4] += descuentos["5"]
        suma_entradas["5"] += precio - descuentos["5"]
sumaTotal=(suma_entradas["1"]+suma_entradas["2"]+suma_entradas["3"]+suma_entradas["4"]+suma_entradas["5"])
sumaTotalDesc=(suma_descuentos[0]+suma_descuentos[1]+suma_descuentos[2]+suma_descuentos[3]+suma_descuentos[4])

print("LA SUMA TOTAL PERCIBIDA ES : $", sumaTotal)
print("EL MONTO TOTAL QUE DEJARÍA DE COBRAR POR EL EVENTO : $",suma_descuentos[0]+suma_descuentos[1]+suma_descuentos[2]+suma_descuentos[3]+suma_descuentos[4])
print("EL MONTO TOTAL QUE DEJARÍA DE COBRAR POR EL EVENTO EN PORCENTAJE SERÍA : ", (sumaTotalDesc/monto)*100,"%")
print("SE PUDO HABER OBTENIDO SI SE HUBIERA COBRADO EL DESCUENTO UN TOTAL DE: ",sumaTotal+sumaTotalDesc)
                 
porcentaje1 = ((clasificación["PRIMERA"] / capacidad)*100)
porcentaje2 = ((clasificación["SEGUNDA"] / capacidad)*100)
porcentaje3 = ((clasificación["TERCERA"] / capacidad)*100)
porcentaje4 = ((clasificación["CUARTA"] / capacidad)*100)
porcentaje5 = ((clasificación["QUINTA"] / capacidad)*100)

if porcentaje1 >0 and porcentaje1 <10 :
    bar1=("**")
elif porcentaje1 >10 and porcentaje1 <15 :
    bar1=("****")
elif porcentaje1 >15 and porcentaje1 <30 :
    bar1=("******")
elif porcentaje1 >30 and porcentaje1 <50 :
    bar1=("********")
elif porcentaje1 >50 and porcentaje1 <100 :
    bar1=("**********")
if porcentaje2 >0 and porcentaje2 <10 :
    bar2=("**")
elif porcentaje2 >10 and porcentaje2 <15 :
    bar2=("****")
elif porcentaje2 >15 and porcentaje2 <30 :
    bar2=("******")
elif porcentaje2 >30 and porcentaje2 <50 :
    bar2=("********")
elif porcentaje1 >50 and porcentaje2 <100 :
    bar2=("**********")
if porcentaje3 >0 and porcentaje3 <10 :
    bar3=("**")
elif porcentaje3 >10 and porcentaje3 <15 :
    bar3=("****")
elif porcentaje3 >15 and porcentaje3 <30 :
    bar3=("******")
elif porcentaje3 >30 and porcentaje <50 :
    bar3=("********")
elif porcentaje3 >50 and porcentaje3 <100 :
    bar3=("**********")
if porcentaje4 >0 and porcentaje4 <10 :
    bar4=("**")
elif porcentaje4 >10 and porcentaje4 <15 :
    bar4=("****")
elif porcentaje4 >15 and porcentaje4 <30 :
    bar4=("******")
elif porcentaje4 >30 and porcentaje4 <50 :
    bar4=("********")
elif porcentaje4 >50 and porcentaje4 <100 :
    bar4=("**********")
if porcentaje5 >0 and porcentaje1 <10 :
    bar5=("**")
elif porcentaje5 >10 and porcentaje5 <15 :
    bar5=("****")
elif porcentaje5 >15 and porcentaje5 <30 :
    bar5=("******")
elif porcentaje5 >30 and porcentaje5 <50 :
    bar5=("********")
if porcentaje5 >50 and porcentaje5 <100 :
    bar5=("**********")
    
    
    
print("RANGO DE EDAD DE LAS PERSONAS QUE ENTRARON:")
print("5-14 :", clasificación["PRIMERA"], porcentaje1, "%", "=",bar1)
print("15-19 :", clasificación["SEGUNDA"], porcentaje2, "%", "=",bar2)
print("20-45 :", clasificación["TERCERA"], porcentaje3, "%", "=",bar3)
print("46-65 :", clasificación["CUARTA"], porcentaje4, "%", "=",bar4)
print("66-> :", clasificación["QUINTA"], porcentaje5, "%", "=",bar5)
