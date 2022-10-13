
import math

degree = "DEG" 

log10Fun = lambda i: math.log(i,10)
#sintaxis lambda: variable_name = lambda parameters : expression if(condition) else expression
#sinFun = lambda i:round(math.sin(i),10) if degree == "RAD" else round(math.sin(math.radians(i)),10)
#cosFun = lambda i:round(math.cos(i),10) if degree == "RAD" else round(math.cos(math.radians(i)),10)
#tanFun = lambda i:round(math.tan(i),10) if degree == "RAD" else round(math.tan(math.radians(i)),10)

def sinFun(i):
    if degree == "RAD":
        return round(math.sin(i),10)
    else:
        return round(math.sin(math.radians(i)),10)

def cosFun(i):
    if degree == "RAD":
        return round(math.cos(i),10)
    else:
        return round(math.cos(math.radians(i)),10)

def tanFun(i):
    infinite = "IND"
    if degree == "RAD" and i%math.radians(90) == 0 and i%math.radians(180) != 0:
        return infinite
    elif degree == "DEG" and i%90 == 0 and i%180 != 0:
        return infinite
    elif degree == "RAD" and i%math.radians(180) != 90:
        return round(math.tan(i),10)
    elif degree == "DEG" and i%180 != 90:
        return round(math.tan(math.radians(i)),10)

class Essentials:
    
    

    def __init__(self):
        self.result = 0
        self.text_calc = "0"
        self.opPlace = '0'
        self.pulses = 0
        self.numbers = (0,1,2,3,4,5,6,7,8,9)
        self.operators = {"+","-","x","÷","^"}
        self.operators2 = {"+","-","*","/"}
        self.parenthesis = ["(",")"]
        self.display = "0" 
        self.degree = "DEG"
    
    

    #Botones De Numeros:
    def sudoButton(self,n):
        if self.opPlace == "0":
            self.opPlace = str(n)
        elif self.opPlace.endswith(")"):
            self.opPlace = self.opPlace+"*"+str(n)
        else:
            self.opPlace = self.opPlace + str(n)
        
        if self.display == "0":
            self.display = str(n)
        elif self.display.endswith(")"):
            self.display = self.display+"x"+str(n)
        else:
            self.display = self.display + str(n)
  
    # Botones De Funciones principales:

    def Add(self):
        self.opPlace = self.opPlace + "+"
        self.display = self.display + "+"
        self.pulses = 0


    def Div(self):
        if self.opPlace[-1] in self.operators2:
            self.opPlace = self.opPlace[:-1]+"/"
        else:
            self.opPlace = self.opPlace + "/"
        
        if self.display[-1] in self.operators:
            self.display = self.display[:-1]+"÷"
        else:
            self.display = self.display + "÷"
        
        self.pulses = 0

    def Multi(self):
        if self.opPlace[-1] in self.operators2:
            self.opPlace = self.opPlace[:-1]+"*"
        else:
            self.opPlace = self.opPlace + "*"
        
        if self.display[-1] in self.operators:
            self.display = self.display[:-1]+"x"
        else:
            self.display = self.display + "x"
        self.pulses = 0

    def AC(self):
        self.opPlace = "0"
        self.text_calc = "0"
        self.display = "0"
        self.wall1 = "0"
        self.result = 0

    def Sub(self):
        self.opPlace = self.opPlace + "-"
        self.display = self.display + "-"
        self.pulses = 0
    
    

    def Result(self,pi,eu):
  
        #resultado                        
        for i in self.opPlace:
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
            elif i == "(" and self.opPlace.startswith("(") and self.pulses == 0:
                self.text_calc = str(i)
                self.pulses +=1
            elif i == "r" and self.opPlace.startswith("r") and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "l" and self.opPlace.startswith("l")and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "L" and self.opPlace.startswith("L")and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "s" and self.opPlace.startswith("s")and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "c" and self.opPlace.startswith("c")and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "t" and self.opPlace.startswith("t")and self.text_calc == "0":
                self.text_calc = str(i)
            else:
                self.text_calc = self.text_calc + str(i)
        self.result = eval(self.text_calc,{},{"r":math.sqrt,"l":math.log,"L":log10Fun,"s":sinFun,"c":cosFun,"t":tanFun}) #se añade sqrt como r para locals de eval
        self.display = str(self.result)
        self.text_calc = "0" #temporal
        self.pulses = 0
        
    def Open_Par(self):
        self.pulses = 0
        if self.display[-1] in self.operators:
            self.display = self.display + "("
        elif self.display.endswith("("):
            self.display = self.display + "+("
        else:
            self.display = self.display + "x("

        if self.opPlace[-1] in self.operators2:
            self.opPlace = self.opPlace + "("
        elif self.opPlace.endswith("("):
            self.opPlace = self.opPlace + "+("
        else:
            self.opPlace = self.opPlace + "*("
        
    def Close_Par(self):

        self.opPlace = self.opPlace + ")"
        self.display = self.display + ")"

    def Point(self):
        
        if self.pulses == 0:
            self.opPlace = self.opPlace + "."
            self.display = self.display + "."
            self.pulses = 1
        else:
            pass


    '''Cientifica'''
    
    def piButton(self, x):
        
        if self.opPlace == "0" :
            self.opPlace = str(x)
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*"+str(x)
        elif self.opPlace[-1] in self.operators2:
            self.opPlace = self.opPlace + str(x)
        elif self.opPlace[-1] == ")":
            self.opPlace = self.opPlace + "*"+str(x)
        else:
            self.opPlace = self.opPlace + str(x)

        if self.display == "0" :
            self.display = str(x)
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "x"+str(x) 
        elif self.display[-1] in self.operators:
            self.display = self.display + str(x)
        elif self.display[-1] == ")":
            self.display = self.display + "x"+str(x) 
        else:
            self.display = self.display + str(x)

    def eulerButton(self, e):
        if self.opPlace == "0" :
            self.opPlace = str(e)
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*"+str(e)
        elif self.opPlace[-1] in self.operators2:
            self.opPlace = self.opPlace + str(e)
        elif self.opPlace[-1] == ")":
            self.opPlace = self.opPlace + "*"+str(e)
        else:
            self.opPlace = self.opPlace + str(e)

        if self.display == "0" :
            self.display = str(e)
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "x"+str(e) 
        elif self.display[-1] in self.operators:
            self.display = self.display + str(e)
        elif self.display[-1] == ")":
            self.display = self.display + "x"+str(e) 
        else:
            self.display = self.display + str(e)

    def squarePow(self):
        self.opPlace = self.opPlace + "^2"
        self.display = self.display + "^2"
    def powe(self):
        self.opPlace = self.opPlace + "**"
        self.display = self.display + "^"
    
    def root(self):
        if self.opPlace == "0":
            self.opPlace = "r("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*r("
        else:
            self.opPlace = self.opPlace + "r("
        
        if self.display == "0":
            self.display = "√("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "x√("
        else:
            self.display = self.display + "√("
    def ln(self):
        if self.opPlace == "0":
            self.opPlace = "l("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*l("
        
        if self.display == "0":
            self.display = "ln("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xln("
        else:
            self.display = self.display + "ln("
    

    def log(self):
        if self.opPlace == "0":
            self.opPlace = "L("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*L("
        else:
            self.opPlace = self.opPlace + "L("
        
        if self.display == "0":
            self.display = "log("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xlog("
        else:
            self.display = self.display + "log("
    def radOrDeg(self):
        global degree
        if degree == "DEG":
            degree = "RAD"
        else:
            degree = "DEG"
   
    def sin(self):
        if self.opPlace == "0":
            self.opPlace = "s("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*s("
        else:
            self.opPlace = self.display + "s("
        
        if self.display == "0":
            self.display = "sin("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xsin("
        else:
            self.display = self.display + "sin("
    
    def cos(self):
        if self.opPlace == "0":
            self.opPlace = "c("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*c("
        else:
            self.opPlace = self.display + "c("
        
        if self.display == "0":
            self.display = "cos("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xcos("
        else:
            self.display = self.display + "cos("
    def tan(self):
        if self.opPlace == "0":
            self.opPlace = "t("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*t("
        else:
            self.opPlace = self.display + "t("
        
        if self.display == "0":
            self.display = "tan("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xtan("
        else:
            self.display = self.display + "tan("   
        
