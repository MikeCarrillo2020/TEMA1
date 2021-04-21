#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: PRACTICA_3.4_PRACTICANDO CLASES Y OBJETOS
class Empleado:
    def _init_(self, nombre, edad, legajo, sueldo):
        self.nombre=nombre
        self.edad=edad
        self.legajo=legajo
        self.sueldoBase=sueldo
    def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase-descuentos+bonos
