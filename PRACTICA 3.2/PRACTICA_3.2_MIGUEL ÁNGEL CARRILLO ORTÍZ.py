#Nombre: Miguel Ángel Carrillo Ortíz
#Carrera: Informática
#Materia: Desarrollo de Aplicaciones Web
#Ejercicio o Práctica: PRACTICA 3.2 - PRACTICANDO CONDICIONALES COMPLEJAS PYTHON
fecha=input("fecha(formato ´dia, DD/MM´):")#(ESTO SE CONSIDERA CÓMO UN STRING LITERAL ) Aquí indicó que ingrese DOS DÍGITOS PARA EL DÍA Y DOS PARA EL MES 
fecha=fecha.lower()#Esto convierte las minúsculas las letras pero si ya están en minúsculas no afectará en nada
diasemana=fecha[0:fecha.find(",")]#Aquí extraremos los días de la semana,también indico que empieze del cero hasta el x número de letras tendrá el día que ingrese para que la coma se coloque
dianro=int(fecha[fecha.find(" ")+1:fecha.find("/")]) #Aquí iniciamos en DD y en lugar de la cómo buscará la barra así iniciará uno antes de la barra
mesnro=int(fecha[fecha.find("/")+1:])#Aquí representamos el mes #Aquí mostraremos uno después de la bara así como para el día empezabamos uno después del espacio
if dianro>31 or mesnro>12:#Aquí colocamos la condición que marcará la condición incorrecta
    print("Fecha incorrecta")
else:# Aquí si la condición es correcta continuara 
    if diasemana in "lunes, martes, miércoles":#Aquí preguntará los de la semana es, aquí se preguntará si se tomaron exámenes lunes, martes o el miércoles 
        respuesta=input("¿Se tomaron exámenes? S/N:")
        if respuesta.lower()=="s":
            aprobados=int(input("Cantidad de aprobados:"))
            reprobados=int(input("Cantidad de reprobados:"))
            print("Porcentaje de aprobados:", (aprobados*100)/(aprobados+reprobados) ,"s" )#Aquí calcularemos el porcentaje de aprobados y reprobados 
    elif diasemana =="jueves":#Sí el día de la semana se escribe jueves se hará otra cosa que es el siguiente código
        asistencia=int(input("Porcentaje de asistencia:"))#Este es el código que se ejecuta cuando introducimos el día jueves
        if asistencia>50:  #Sí es mayor nos dirá no asistió la mayoría y si es menor de 50 pues nos dirá asistió la mayoría
            print("Asistencia la mayoría")
        else: print("No asistió la mayoría")
    elif diasemana =="viernes":#Aquí en viernes en esta parte nos dirá que se inicio un nuevo ciclo al colocar 1/7
        if dianro==1 and (mesnro==1 or mesnro==7):
            print("Comienzo de nuevo ciclo")
            alumno=int(input("Cantidad de alumnos:"))#Nos pedirá el número de alumnos
            arancel=float(input("arancel:$"))#Aquí escribiremos el arancel
            print("Ingreso total:$", alumno*arancel)#Nos arrojará el total del arancel y se finalizará el programa
    else:
        print("Fecha incorrecta ")

print("Fin del programa ")      
