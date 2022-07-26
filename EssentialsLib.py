from math import pi
import math
class Essentials:
    
    def __init__(self):
        self.result = 0
        self.text_calc = "0"
        self.pulses = 0
        
    
    #Botones De Numeros:
    def sudoButton(self,n):
        if self.text_calc == "0":
            self.text_calc = str(n)
        elif self.text_calc.endswith(")"):
            self.text_calc = self.text_calc+"*"+str(n)
        else:
            self.text_calc = self.text_calc + str(n)
  
    # Botones De Funciones principales:

    def Add(self):
        self.text_calc
        self.text_calc = self.text_calc + "+"
        self.pulses = 0

    def Div(self):
        self.text_calc
        self.text_calc = self.text_calc + "/"
        self.pulses = 0

    def Multi(self):
        self.text_calc
        self.text_calc = self.text_calc + "*"
        self.pulses = 0

    def AC(self):
        
        self.text_calc
        self.text_calc = "0"

    def Sub(self):
        self.text_calc
        self.text_calc = self.text_calc + "-"
        self.pulses = 0

    def Result(self):
        self.result = eval(self.text_calc)
        self.text_calc = str(self.result)
        self.pulses = 0
        
    def Open_Par(self):
        self.pulses = 0
        if self.text_calc.endswith("-") or self.text_calc.endswith("+"):
            self.text_calc = self.text_calc + "("
        else:
            self.text_calc = self.text_calc + "*("
        
    def Close_Par(self):

        self.text_calc = self.text_calc + ")"

    def Point(self):
        
        if self.pulses == 0:
            self.text_calc = self.text_calc + "."
            self.pulses = 1
        else:
            pass

    def Neg_or_Pos(self):
        pass

    '''Cientifica'''
    def piButton(self, x):
        
        if self.text_calc == "0" :
            self.text_calc = str(x)
        elif self.text_calc.endswith("(")or self.text_calc.endswith("+") or self.text_calc.endswith("-") or self.text_calc.endswith("*")or self.text_calc.endswith("/"):
            self.text_calc = self.text_calc + str(x)
        else:
            self.text_calc = self.text_calc + "*"+str(x)

    def square(self):
        self.text_calc = self.text_calc + "**2"

    def powe(self):
        self.text_calc = self.text_calc + "**"
    
    
   