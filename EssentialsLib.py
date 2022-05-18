
class Essentials:
    
    def __init__(self):
        self.result = 0
        self.text_calc = "0"
    
   
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
            self.text_calc = "6"
        else:
            self.text_calc = self.text_calc + "9"
    def Button0(self):
        
        if self.text_calc != "0":
            self.text_calc = self.text_calc + "0"
    def Add(self):
        self.text_calc
        self.text_calc = self.text_calc + "+"
    def Sub(self):
        
        self.text_calc = self.text_calc + "-"
    def Result(self):
        
        self.result = eval(self.text_calc)

