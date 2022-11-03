import math
import numpy as np
from numpy import arange



degree = "DEG" 

log10Fun = lambda i: math.log(i,10)
lnFun = lambda i: math.log(i,math.e)
#sintaxis lambda: variable_name = lambda parameters : expression if(condition) else expression
#sinFun = lambda i:round(math.sin(i),10) if degree == "RAD" else round(math.sin(math.radians(i)),10)
#cosFun = lambda i:round(math.cos(i),10) if degree == "RAD" else round(math.cos(math.radians(i)),10)
#tanFun = lambda i:round(math.tan(i),10) if degree == "RAD" else round(math.tan(math.radians(i)),10)

def sinFun(i):
    if degree == "RAD":
        x = round(math.sin(i),10)
        return x
    else:
        x = round(math.sin(math.radians(i)),10)
        return x

def cosFun(i):
    if degree == "RAD":
        x = round(math.cos(i),10)
        return x
    else:
        x = round(math.cos(math.radians(i)),10)
        return x

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

def cscFun(i): #1/sin
    infinite = "IND"
    if degree == "RAD" and i%math.radians(180) == 0:
        return infinite
    elif degree == "DEG" and i%180 == 0:
        return infinite
    elif degree == "RAD" and i%math.radians(180) != 0:
        return round(1/sinFun(i),10)
    elif degree == "DEG" and i%180 != 0:
        return round(1/sinFun(i),10)
    
def secFun(i): #1/cos
    infinite = "IND"
    if degree == "RAD" and i%math.radians(90) == 0 and i%math.radians(180) != 0:
        return infinite
    elif degree == "DEG" and i%90 == 0 and i%180 != 0:
        return infinite
    elif degree == "RAD" and i%math.radians(180) != 90:
        return round(1/cosFun(i),10)
    elif degree == "DEG" and i%180 != 90:
        return round(1/cosFun(i),10)

def cotFun(i): #Cos/Sin
    infinite = "IND"
    if degree == "RAD" and i%math.radians(180) == 0:
        return infinite
    elif degree == "DEG" and i%180 == 0:
        return infinite
    elif degree == "RAD" and i%math.radians(180) != 0:
        return round(1/tanFun(i),10)
    elif degree == "DEG" and i%180 != 0:
        return round(1/tanFun(i),10)
def factorial(x):
    f = 1.0
    for i in np.arange(1.0,x+1.0):
        f = f*i
    return f 


absoluteValue = lambda i: abs(i)



class Essentials:
    
    

    def __init__(self):
        self.result = 0
        self.text_calc = "0"
        self.opPlace = '0'
        self.pulses = 0
        self.numbers = ["0","1","2","3","4","5","6","7","8","9"]
        self.operators = {"+","-","x","÷","^"}
        self.operators2 = {"+","-","*","/"}
        self.parenthesis = ["(",")"]
        self.display = "0" 
        self.degree = "DEG"
        self.fourFuns = ("log(","sin(","cos(","tan(","abs(","fac(")
        self.exce = ""
        self.funs = ['+','-','x','^','÷','(',')','','ln(',"log(","sin(","cos(","tan(","abs(,√("]
        self.dictFuns = {"r":math.sqrt,
        "l":lnFun,
        "L":log10Fun,
        "s":sinFun, "S": secFun,
        "c":cosFun, "C": cscFun,
        "t":tanFun, "T": cotFun,
        "a":absoluteValue,
        "e":math.e,
        "π":math.pi,
        "f":factorial
        }
    

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
        return self.display

    def doubleZero(self):
        if self.opPlace == "0":
            self.opPlace = str(0)
        elif self.opPlace.endswith(")"):
            self.opPlace = self.opPlace+"*"+"0"
        elif len(self.opPlace) > 1 and self.opPlace[-2] in self.operators2 and self.opPlace[-1] == "0":
            self.opPlace = self.opPlace
        elif self.display[-1] in self.operators2:
            self.display = self.opPlace + "0"
        else:
            self.opPlace = self.opPlace + "00"
        
        if self.display == "0":
            self.display = str(0)
        elif self.display.endswith(")"):
            self.display = self.display+"x"+"0"
        elif len(self.display) > 1 and self.display[-2] in self.operators and self.display[-1] == "0":
            self.display = self.display
        elif self.display[-1] in self.operators:
            self.display = self.display + "0"                         
        else:
            self.display = self.display + "00"
        return self.display
  
    # Botones De Funciones principales:

    def Add(self):
        self.opPlace = self.opPlace + "+"
        self.display = self.display + "+"
        self.pulses = 0
        return self.display


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
        return self.display
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
        return self.display
    def AC(self):
        self.opPlace = "0"
        self.text_calc = "0"
        self.display = "0"
        self.wall1 = "0"
        self.result = 0
        self.pulses = 0
        return self.display
    def Sub(self):
        self.opPlace = self.opPlace + "-"
        self.display = self.display + "-"
        self.pulses = 0
        return self.display
    def Remainder(self):
        if self.opPlace[-1] in self.operators2:
            self.opPlace = self.opPlace[:-1]+"%"
        else:
            self.opPlace = self.opPlace + "%"
        
        if self.display[-1] in self.operators:
            self.display = self.display[:-1]+"%"
        else:
            self.display = self.display + "%"
        
        self.pulses = 0
        return self.display
    

    def Result(self):
  
        #resultado       
        
        for i in self.opPlace:
            if i in str(self.numbers):
                if self.text_calc == "0":
                    self.text_calc = str(i)
                elif self.text_calc.endswith(")"):
                    self.text_calc = self.text_calc+"*"+str(i)
                else:
                    self.text_calc = self.text_calc + str(i)      
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
            elif i == "S" and self.opPlace.startswith("S")and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "C" and self.opPlace.startswith("C")and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "T" and self.opPlace.startswith("T")and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "a" and self.opPlace.startswith("a")and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "f" and self.opPlace.startswith("f")and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "e" and self.opPlace.startswith("e")and self.text_calc == "0":
                self.text_calc = str(i)
            elif i == "π" and self.opPlace.startswith("π")and self.text_calc == "0":
                self.text_calc = str(i)
            else:
                self.text_calc = self.text_calc + str(i)
        try:
            self.result = eval(str(self.text_calc),self.dictFuns,) #se añade sqrt como r para locals de eval
        except ZeroDivisionError:
            self.text_calc = "0"
            self.exce = "Can't Divide By Zero"
            self.opPlace = "0"
            self.display = "0"
            return self.exce
        except ValueError:
            self.text_calc = "0"
            self.exce = "Error"
            self.opPlace = "0"
            self.display = "0"
            return self.exce
        except SyntaxError:
            self.exce = "Parenthe(sis/ses) Not Closed"
            self.result = "0"
            return self.exce
        else:
            if self.result == "IND":
                self.display = "0"
                self.opPlace = "0"
            else:
                self.display = str(self.result)
                self.opPlace = str(self.result)
            self.text_calc = "0" #temporal
            self.pulses = 0
            return self.result
        finally:
            self.exce = ""
        
            
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
        return self.display
        
    def Close_Par(self):
        self.pulses = 0
        self.opPlace = self.opPlace + ")"
        self.display = self.display + ")"
        return self.display

    def Point(self):
        bwdsdisplay = ""
        for i in reversed(self.display):
            if i == ".":
                bwdsdisplay = bwdsdisplay + i
                break
            elif i in self.funs:
                break
            else:
                bwdsdisplay = bwdsdisplay + i

        if "." in bwdsdisplay:
            if any(ext in bwdsdisplay for ext in self.funs):   #if self.funs in bwdsdisplay:
                self.pulses = 0
            else:
                self.pulses = 1
        else:
            if self.pulses == 0 and self.display[-1] in self.numbers:
                self.opPlace = self.opPlace + "."
                self.display = self.display + "."
                self.pulses = 1
            elif self.display[-1] in self.operators2:
                self.opPlace = self.opPlace +"0."
                self.display = self.display +"0."
                self.pulses = 1
            elif self.display[-1] in self.parenthesis:
                self.opPlace = self.opPlace + "*0."
                self.display = self.display + "x0."
            else:
                pass
        return self.display


    '''Cientifica'''
    
    def piButton(self, x):
        
        if self.opPlace == "0" :
            self.opPlace = str(x)
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*"+str(x)
            self.pulses = 0
        elif self.opPlace[-1] in self.operators2:
            self.opPlace = self.opPlace + str(x)
        elif self.opPlace[-1] == ")":
            self.opPlace = self.opPlace + "*"+str(x)
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*"+str(x)
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
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"x"+str(x)
        else:
            self.display = self.display + str(x)
        return self.display

    def eulerButton(self, e):
        if self.opPlace == "0" :
            self.opPlace = str(e)
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*"+str(e)
        elif self.opPlace[-1] in self.operators2:
            self.opPlace = self.opPlace + str(e)
        elif self.opPlace[-1] == ")":
            self.opPlace = self.opPlace + "*"+str(e)
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*"+str(e)
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
        elif self.display[-1] == ")":
            self.display = self.display + "x"+str(e) 
        else:
            self.display = self.display + str(e)
        return self.display

    def squarePow(self):
        self.opPlace = self.opPlace + "^2"
        self.display = self.display + "^2"
        return self.display

    def powe(self):
        self.opPlace = self.opPlace + "**"
        self.display = self.display + "^"
        return self.display
    
    def root(self):
        if self.opPlace == "0":
            self.opPlace = "r("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*r("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*r("
        else:
            self.opPlace = self.opPlace + "r("
        
        if self.display == "0":
            self.display = "√("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "x√("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"x√("
        else:
            self.display = self.display + "√("
        return self.display
        
    def ln(self):
        if self.opPlace == "0":
            self.opPlace = "l("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*l("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*l("
        else:
            self.opPlace = self.opPlace + "l("
        
        if self.display == "0":
            self.display = "ln("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xln("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"xln("
        else:
            self.display = self.display + "ln("
        return self.display

    def log(self):
        if self.opPlace == "0":
            self.opPlace = "L("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*L("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*L("
        else:
            self.opPlace = self.opPlace + "L("
        
        if self.display == "0":
            self.display = "log("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xlog("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"xlog("
        else:
            self.display = self.display + "log("
        return self.display

    def radOrDeg(self):
        global degree
        if degree == "DEG":
            degree = "RAD"
        else:
            degree = "DEG"
        return degree
   
    def sin(self):
        if self.opPlace == "0":
            self.opPlace = "s("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*s("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*s("
        else:
            self.opPlace = self.opPlace + "s("
        
        if self.display == "0":
            self.display = "sin("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xsin("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"xsin("
        else:
            self.display = self.display + "sin("
        return self.display
    
    def cos(self):
        if self.opPlace == "0":
            self.opPlace = "c("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*c("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*c("
        else:
            self.opPlace = self.opPlace + "c("
        
        if self.display == "0":
            self.display = "cos("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xcos("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"xcos("
        else:
            self.display = self.display + "cos("
        return self.display

    def tan(self):
        if self.opPlace == "0":
            self.opPlace = "t("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*t("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*t("            
        else:
            self.opPlace = self.opPlace + "t("
        
        if self.display == "0":
            self.display = "tan("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xtan("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"xtan("
        else:
            self.display = self.display + "tan("
        return self.display

    def csc(self):
        if self.opPlace == "0":
            self.opPlace = "C("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*C("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*C("            
        else:
            self.opPlace = self.opPlace + "C("
        
        if self.display == "0":
            self.display = "csc("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xcsc("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"xcsc("
        else:
            self.display = self.display + "csc("
        return self.display

    def sec(self):
        if self.opPlace == "0":
            self.opPlace = "S("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*S("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*S("            
        else:
            self.opPlace = self.opPlace + "S("
        
        if self.display == "0":
            self.display = "sec("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xsec("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"xsec("
        else:
            self.display = self.display + "sec("
        return self.display
    
    def cot(self):
        if self.opPlace == "0":
            self.opPlace = "T("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace + "*T("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*T("            
        else:
            self.opPlace = self.opPlace + "T("
        
        if self.display == "0":
            self.display = "cot("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xcot("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"xcot("
        else:
            self.display = self.display + "cot("
        return self.display

    def abs(self):
        if self.opPlace == "0":
            self.opPlace = "a("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace = "*a("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*a("  
        else:
            self.opPlace = self.opPlace + "a("

        if self.display == "0":
            self.display = "abs("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "xabs("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"xabs("
        else:
            self.display = self.display + "abs("
        return self.display
    
    def fact(self):
        if self.opPlace == "0":
            self.opPlace = "f("
        elif self.opPlace[-1] in str(self.numbers):
            self.opPlace = self.opPlace = "*f("
        elif self.opPlace[-1] == ".":
            self.opPlace = self.opPlace +"0"+"*f("  
        else:
            self.opPlace = self.opPlace + "f("

        if self.display == "0":
            self.display = "!("
        elif self.display[-1] in str(self.numbers):
            self.display = self.display + "x!("
        elif self.display[-1] == ".":
            self.display = self.display +"0"+"x!("
        else:
            self.display = self.display + "!("
        return self.display
         
    def erase(self):
        if self.display[-4:] in self.fourFuns and len(self.display) > 4:
            self.opPlace = self.opPlace[:-2]
            self.display = self.display[:-4]
        elif self.display[-1] == ".":
            self.opPlace = self.opPlace[:-1]
            self.display = self.display[:-1]
            self.pulses = 0
        elif self.display[-4:] in self.fourFuns and len(self.display) == 4:
            self.opPlace = "0"
            self.display = "0"
        elif self.display[-3:] == "ln(" and len(self.display) >3:
            self.opPlace = self.opPlace[:-2]
            self.display = self.display[:-3]
        elif self.display[-3:] == "ln(" and len(self.display) ==3:
            self.opPlace = "0"
            self.display = "0"
        elif self.display[-2:] == "√(" and len(self.display) >2:
            self.opPlace = self.opPlace[:-2]
            self.display = self.display[:-2]
        elif self.display[-2:] == "√(" and len(self.display) ==2:
            self.opPlace = "0"
            self.display = "0"
        elif len(self.display) ==1:
            self.opPlace = "0"
            self.display = "0"
        else:
            self.opPlace = self.opPlace[:-1]
            self.display = self.display[:-1]
        return self.display