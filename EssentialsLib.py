import math


class Essentials:
    
    def __init__(self):
        self.result = 0
        self.text_calc = "0"
        self.opPlace = '0'
        self.pulses = 0
        self.numbers = {1,2,3,4,5,6,7,8,9,"π","e"}
        self.operators = {"+","-","x","÷"}
        self.parenthesis = ["(",")"]
        self.wall1 = "0"
        self.temp = "0"
        self.tempy = 0
        
    
    #Botones De Numeros:
    def sudoButton(self,n):
        if self.opPlace == "0":
            self.opPlace = str(n)
        elif self.opPlace.endswith(")"):
            self.opPlace = self.opPlace+"x"+str(n)
        else:
            self.opPlace = self.opPlace + str(n)
  
    # Botones De Funciones principales:

    def Add(self):
        self.opPlace
        self.opPlace = self.opPlace + "+"
        self.pulses = 0

    def Div(self):
        self.opPlace
        self.opPlace = self.opPlace + "÷"
        self.pulses = 0

    def Multi(self):
        self.opPlace
        self.opPlace = self.opPlace + "x"
        self.pulses = 0

    def AC(self):
        
        self.opPlace
        self.opPlace = "0"
        self.text_calc = "0"
        self.wall1 = "0"
        self.result = 0

    def Sub(self):
        self.opPlace
        self.opPlace = self.opPlace + "-"
        self.pulses = 0

    def Result(self,pi,eu):
        #pared 1
        copy = ''+self.opPlace 
        #ejemplo: 100+√((2)+(4))
        while "√" in copy :

            x = self.opPlace.index("√")
            for num,i in enumerate(self.opPlace[x+1:]):
                
                if i == "(" and self.opPlace[x+1:].startswith("(") and self.temp == "0":
                    self.pulses +=1
                    self.temp = i
                elif i == "(":
                    self.pulses +=1
                    self.temp = self.temp+i
                elif i == ")" and self.pulses != 1:
                    self.temp = self.temp+i
                    self.pulses -= 1
                elif i == ")" and self.pulses == 1:
                    self.temp = self.temp+i
                    self.tempy = num
                    self.pulses = 0
                    break
                else:
                    self.temp = self.temp+i
            if x == 0:
                self.wall1 = ''+str(math.sqrt(eval(self.temp)))
                self.temp = "0"
                break
            else:
                self.wall1 = str(self.opPlace[:x])+str(math.sqrt(eval(self.temp)))
        
                
        
        #resultado                        
        for i in self.wall1:
            if i in str(self.numbers):
                if self.text_calc == "0":
                    self.text_calc = str(i)
                elif self.text_calc.endswith(")"):
                    self.text_calc = self.text_calc+"*"+str(i)
                else:
                    self.text_calc = self.text_calc + str(i)      

            elif i == "π":
                if self.text_calc == "0":
                    self.text_calc = str(pi)
                elif self.text_calc.endswith(")"):
                    self.text_calc = self.text_calc+"*"+str(pi)
                else:
                    self.text_calc = self.text_calc + str(pi)
            elif i == "e":
                if self.text_calc == "0":
                    self.text_calc = str(eu)
                elif self.text_calc.endswith(")"):
                    self.text_calc = self.text_calc+"*"+str(pi)
                else:
                    self.text_calc = self.text_calc + str(pi)
            elif i == "x":
                self.text_calc = self.text_calc + "*"
            elif i == "÷":
                self.text_calc = self.text_calc + "/"
            elif i == "^":
                self.text_calc = self.text_calc + "**"
            elif i == "(" and self.wall1.startswith("(") and self.pulses == 0:
                self.text_calc = str(i)
                self.pulses +=1
            else:
                self.text_calc = self.text_calc + str(i)

        self.result = eval(self.text_calc)
        self.opPlace = str(self.result)
        self.pulses = 0
        
    def Open_Par(self):
        self.pulses = 0
        if self.opPlace.endswith("-") or self.opPlace.endswith("+"):
            self.opPlace = self.opPlace + "("
        elif self.opPlace.endswith("("):
            self.opPlace = self.opPlace + "+("
        else:
            self.opPlace = self.opPlace + "x("
        
    def Close_Par(self):

        self.opPlace = self.opPlace + ")"

    def Point(self):
        
        if self.pulses == 0:
            self.opPlace = self.opPlace + "."
            self.pulses = 1
        else:
            pass

    def Neg_or_Pos(self):
        pass

    '''Cientifica'''
    def piButton(self, x):
        
        if self.opPlace == "0" :
            self.opPlace = str(x)
        elif self.opPlace.endswith("(")or self.opPlace.endswith("+") or self.opPlace.endswith("-") or self.opPlace.endswith("x")or self.opPlace.endswith("÷"):
            self.opPlace = self.opPlace + str(x)
        else:
            self.opPlace = self.opPlace + "x"+str(x)
    
    def eulerButton(self, e):
        if self.opPlace == "0" :
            self.opPlace = str(e)
        elif self.opPlace.endswith("(")or self.opPlace.endswith("+") or self.opPlace.endswith("-") or self.opPlace.endswith("x")or self.opPlace.endswith("÷"):
            self.opPlace = self.opPlace + str(e)
        else:
            self.opPlace = self.opPlace + "x"+str(e)

    def square(self):
        self.opPlace = self.opPlace + "^2"

    def powe(self):
        self.opPlace = self.opPlace + "^"
    
    def root(self):
        if self.opPlace == "0":
            self.opPlace = "√("
        elif self.opPlace in str(self.numbers):
            self.opPlace = self.opPlace + "x√("
        else:
            self.opPlace = self.opPlace + "√("
        


   