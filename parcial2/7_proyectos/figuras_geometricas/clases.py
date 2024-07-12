
class Figuras:

    def __init__(self,x,y,visible):
        self.x=x
        self.y=y
        self.visible=visible

    def estaVisible(self):
      return self.visible

    def mostrar(self):
      print(f"Los valores de X y Y son: {self.getX()} {self.getY()}, su visibilidad es: {self.getVisible()}")  

    def ocultar(self):
       return visible = False

    def mover(self):
        x=y 
        y=x

    def calcularArea(self):
      area=x*y
      print(f"El area es {area}")


    def getX(self):
      return self.x

    def setX(self,x):
      self.x=x 

    def getY(self):
      return self.y

    def setY(self,y):
      self.y=y 

    def getVisible(self):
      return self.visible

    def setY(self,visible):
      self.visible=vidible

class Rectangulos(Figuras):
    def __init__(self,x,y,visible):
      super().__init__(x,y,visible) 
      __self.alto=alto
      __self.ancho=ancho

    def getAlto(self):
      return self.__alto

    def setAlto(self,alto):
      self.__alto=alto 

    def getAncho(self):
      return self.__ancho

    def setAncho(self,ancho):
      self.__ancho=ancho 

    def ocultar(self):
      return visible = False

    def mostrar(self):
      print(f"Los valores de la altura y anchura son: {self.getAlto()} {self.getAncho()}, su visibilidad es: {self.getVisible()}")  

    def calcularArea(self):
      area=alto*ancho
      print(f"El area es {area}")

class Circulos(Figuras):
    def __init__(self,x,y,visible):
    super().__init__(x,y,visible) 
    __self.radio=radio

    def getRadio(self):
      return self.__radio

    def setRadio(self,radio):
      self.__radio=radio 

    def ocultar(self):
      return visible = False

    def mostrar(self):
      print(f"Los valores del radio son: {self.getRadio()}, su visibilidad es: {self.getVisible()}")  

    def CalcularArea(self):
        pi=3.1416
        radio2=radio*radio
        area=pi*radio2
        print(f"El area es: {area}")

