#FIGURAS GEOMETRICAS


from abc import ABC, abstractmethod
import math


#Clasesotas 
class Figuras(ABC):
    def __init__(self, x, y, visible):
        self.x=x
        self.y=y
        self.visible=visible

    #METODOS

    def estaVisible(self):
        return self.visible

    def mostrar(self):
        self.visible = True
        print("La figura ahora es visible.")

    def ocultar(self):
        self.visible = False
        print("La figura ahora está oculta.")

    def mover(self):
        # Actualizaaaa posicion? apoco si
        print("Tu figura se ha movido 3 puntos a la izquierda")

    def calcularArea(self):
        # Método abstracto se utilizaran aqui?
        pass

    def getx(self):
        return self.x

    def setx(self, x):
        self.x = x

    def gety(self):
        return self.y

    def sety(self, y):
        self.y = y

    def getVisible(self):
        return self.visible

    def setVisible(self, visible):
        self.visible = visible

    def getInfo(self):
        print(f"Posición: ({self.x}, {self.y}), Visible: {self.visible}")

 




class Rectangulos(Figuras):
    def __init__(self, x, y, ancho, altura, visible=True):
        super().__init__(x, y, visible)
        self.ancho=ancho
        self.altura=altura

    # METODOS
    def calcularArea(self):
        return self.ancho * self.altura

    def setancho(self, ancho):
        self.ancho = ancho

    def getancho(self,):
        return self.ancho

    def getaltura(self):
        return self.altura

    def setaltura(self, altura):
        self.altura = altura

    #polimorfismooo
    def getInfo(self):
        super().getInfo()
        print(f"Ancho: {self.ancho}, Altura: {self.altura}, Área: {self.calcularArea()}")


class Circulos(Figuras):
    def __init__(self, x, y, radio, visible=True):
        super().__init__(x, y, visible)
        self.radio=radio

    #metodo abstractooon
    def calcularArea(self):
        return math.pi * self.radio ** 2 

    def getRadio(self):
        return self.radio
    
    def setRadio(self, altura):
        self.radio = radio

    #polimorfismooo
    def getInfo(self):
        super().getInfo()
        print(f"Radio: {self.radio}, Área: {self.calcularArea()}")

        

    





        
    


