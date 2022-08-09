from sympy import I, root


class Essentials:
    
    def __init__(self):
        self.result = 0
        self.text_calc = "0"
        self.opPlace = '0'
        self.pulses = 0
        self.numbers = {1,2,3,4,5,6,7,8,9}
        self.wall1 = "0"
        
    
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
        for i in self.opPlace:
            if self.wall1 == "0" and i != "√":
                self.wall1 = i
            elif self.wall1 != "0" and i != "√" and i != ")":
                self.wall1 = self.wall1 + i
            elif i == ")" and self.pulses == 1:
                self.wall1 = self.wall1 + ")^1÷2)"
                self.pulses = 0
            elif i == "√":
                self.wall1 = self.wall1 + "("
                self.pulses = self.pulses + 1           
            else:
                self.wall1 = self.wall1 + i
                
                '''for rootIndex in self.opPlace[p+1:]:
                    if rootIndex != ")":
                        self.wall1 = self.wall1 + rootIndex
                    else:
                        self.wall1 = self.wall1 + ""'''

            
                        
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
        self.opPlace = self.opPlace + "√("
   