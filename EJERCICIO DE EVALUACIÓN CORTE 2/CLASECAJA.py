#NOMBRE: MIGUEL ÁNGEL CARRILLO ORTÍZ
#CARRERA: INFORMÁTICA
#MATERIA: DESARROLLO DE APLICACIONES WEB
#EJERCICIO O PRÁCTICA: EJERCICIO DE EVALUACIÓN
#Aquí se crea la clase caja
class Caja:
#Aquí se crea el metodo constructor
    def __init__(self, ancho, largo, alto):
        self.ancho=ancho
        self.largo=largo
        self.alto=alto
#Aquí se crea el método mostrar para mostrar los valores de la clase caja    
    def mostrar(self):
        return"ALTO: ",self.alto," ANCHO: ", self.ancho," LARGO: ", self.largo
#Aquí se crea el método para calcular el volumen  
    def calcularVolumen(self):
        Vol = (self.alto * self.ancho * self.largo)
        return("EL VOLUMEN ES: ",Vol)
#Aquí se crea el método para calcular el área lateral   
    def areaLateral(self):
        return self.largo * self.alto
#Aquí se crea el método para calcular el área frontal       
    def areaFrontal(self):
        return self.alto * self.ancho
#Aquí se crea el método para calcular el áreasuperior      
    def areaSuperior(self):
        return self.largo * self.ancho
#Aquí se crea el método para calcular el área total    
    def calcularAreaTotal(self):
        Total = (2 * self.areaFrontal() + 2 * self.areaSuperior() + 2 * self.areaLateral())
        return Total
#Aquí se crea el método para crear un clon de nuestra clase
    def clon(self):
        cl= Caja(self.ancho, self.largo, self.alto)
        return cl
#Aquí se crea un método con valores con un 25% más grande
    def crearCajaGrande(self):
        nuevoAlto = self.alto * 1.25
        nuevoAncho = self.ancho * 1.25
        nuevoLargo  = self.largo * 1.25

        cajaNueva = Caja(nuevoAncho, nuevoLargo, nuevoAlto)
        return cajaNueva
#Aquí se crea un método para comparar el clon con la caja más grande, se comparan los valores para saber si cabe la caja clon con la caja más grande  
    def cabe1DentroDe2(self, cl,cajaNueva):
        if cl.ancho < cajaNueva.ancho and cl.alto < cajaNueva.alto and cl.largo < cajaNueva.largo:
            return "SÍ CABE"
        else:
            return "NO CABE"
