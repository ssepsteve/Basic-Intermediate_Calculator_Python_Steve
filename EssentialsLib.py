
class Essentials:
    
    def __init__(self):
        self.result = 0
        self.text_calc = "0"
        self.pulses = 0
    
    #Botones De Numeros:
    def Button1(self):
         
        if self.text_calc == "0":
            self.text_calc = "1"
        else:
            self.text_calc = self.text_calc + "1"
    def Button2(self):
        if self.text_calc == "0":
            self.text_calc = "2"
        else:
            self.text_calc = self.text_calc + "2"
    def Button3(self):
        
        if self.text_calc == "0":
            self.text_calc = "3"
        else:
            self.text_calc = self.text_calc + "3"        
    def Button4(self):
        
        if self.text_calc == "0":
            self.text_calc = "4"
        else:
            self.text_calc = self.text_calc + "4"        
    def Button5(self):
        
        if self.text_calc == "0":
            self.text_calc = "5"
        else:
            self.text_calc = self.text_calc + "5"
    def Button6(self):
        
        if self.text_calc == "0":
            self.text_calc = "6"
        else:
            self.text_calc = self.text_calc + "6"
    def Button7(self):
        
        if self.text_calc == "0":
            self.text_calc = "7"
        else:
            self.text_calc = self.text_calc + "7"
    def Button8(self):
        
        if self.text_calc == "0":
            self.text_calc = "8"
        else:
            self.text_calc = self.text_calc + "8"
    def Button9(self):
        
        if self.text_calc == "0":
            self.text_calc = "9"
        else:
            self.text_calc = self.text_calc + "9"
    def Button0(self):
        
        if self.text_calc != "0":
            self.text_calc = self.text_calc + "0"
    
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


