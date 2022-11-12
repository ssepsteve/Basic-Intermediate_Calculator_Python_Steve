class Basic: #Se crea la clase con el nombre Basic
    def __init__(self): #Constructor de la variable
        self.opPlace = "0" # Se crea el objeto tipo str que almacenara las operaciones y numeros
        self.operators = ["+","-","*","/"] # Se crea lista con los strings de los operadores
        self.pulses = 0 #cuantas veces se ha pulsado point
        self.signs = self.operators + ["(",")"] # se crea la lista de signos que contiene a los operadores mas los parentesis
    def numFun(self,n): #Creacion funcion de numero
        if self.opPlace == "0": #Sí la variable es igual a cero, hara lo siguiente:
            self.opPlace = str(n)#El objeto sera igual al numero introducido
        elif self.opPlace[-1] == ")": #Si el ultimo caracter es )
            self.operator("*") # se añade una multiplicacion
            self.opPlace = self.opPlace + str(n) #se agrega el numero
        elif n == 0 and self.opPlace[-1] == 0 and self.opPlace[-2] in self.operators or self.opPlace[-2] == "(": #si el numero introducido por el usuario es un 0, el ultimo caracter de la variable es un 0 y el antepenultimo caracter es un operador/parentesis
            pass #no hace nada
        else: #Sí de lo contrario no se cumple la condicion:
            self.opPlace = self.opPlace + str(n) #Se suma el valor dado al objeto
        return self.opPlace
    def operator(self,o:str): #se crea una funcion de operador en donde se tiene que introducir un operador en forma de string
        if self.opPlace[-1] in self.operators: #si el ultimo caracter esta en la lista de operadores
            self.opPlace = self.opPlace[:-1]+o#se borrara el caracter ultimo y se pondra el operador
            self.pulses = 0 #se resetea a 0 cuantas veces se uso point
        else: #De lo contrario
            self.opPlace = self.opPlace +o #añadimos el operador
            self.pulses = 0 #se resetea a 0 cuantas veces se uso point
        return self.opPlace
    def point(self): # se crea la funcion de punto
        bwdsOpPlace = "" # se crea una variable
        for i in reversed(self.opPlace): #cilo for en el reverso de la variable opPlace
            if i == ".": # si i es igual a .
                bwdsOpPlace = bwdsOpPlace + i # se añade i a la variable
                break # se rompe el ciclo 
            elif i in self.operators: #si i es un operador
                break # se rompe el ciclo
            elif i == "(" or i == ")": # si i es un parentesis
                break # se rompe el ciclo
            else: # de lo contrario 
                bwdsOpPlace = bwdsOpPlace + i # se añade i a la variable

        if "." in bwdsOpPlace: # si hay un punto en la variable
            self.pulses == 1 # se habra declarado que se ha usado un punto
        else: # de lo contrario
            if self.opPlace[-1] in self.operators: #si el ultimo caracter esta adentro de la lista de operadores
                self.opPlace = self.opPlace + "0." #se añade un 0. despues del operador
                self.pulses = 1 # se ha pulsado point
            elif self.opPlace[-1] == ")":#sí el ultimo caracter es )
                self.operator("*") #se añade una multiplicacion
                self.opPlace = self.opPlace + "0." #se añade un 0. despues del operador
                self.pulses = 1 # se ha pulsado point
            elif self.opPlace[-1] == "(": # si el ultimo caracter es (
                self.numFun(0) # se añade 0
                self.opPlace = self.opPlace + "." # se añade .
            elif self.pulses == 1: #si se ha pulsado point
                pass # no se hace nada
            else: # de lo contrario
                self.opPlace = self.opPlace + "." #se añade un .
                self.pulses = 1 #se ha pulsado point
        return self.opPlace
    def openPar(self): #se crea la funcion de abrir parentesis
        if self.opPlace[-1] in self.operators: #si el ultimo caracter es un operador
            self.opPlace = self.opPlace + "(" #se añade (
            self.pulses = 0 #se resetea a 0 cuantas veces se uso point
        elif self.opPlace[-1] == ".": #si el ultimo caracter es un punto
            self.numFun(0) # se pone un cero
            self.operator("*") # se pone una multiplicacion
            self.opPlace = self.opPlace + "(" #se añade (
            self.pulses = 0 #se resetea a 0 cuantas veces se uso point
        else: #de lo contrario
            self.operator("*") #se pone una multiplicacion
            self.opPlace = self.opPlace + "(" #se añade (
            self.pulses = 0 #se resetea a 0 cuantas veces se uso point
        return self.opPlace
    def closePar(self):#se crea la funcion de cierre de parentesis
        if self.opPlace[-1] in self.operators: # si el ultimo caracter es operador
            self.opPlace = self.opPlace[:-1] + ")" #se quita el ultimo caracter y se añade un )
        elif self.opPlace[-1] == ".": # si el ultimo caracter es un .
            self.numFun(0)#se añade un 0
            self.opPlace = self.opPlace + ")"# se añade un )
        else: #de lo contrario
            self.opPlace = self.opPlace + ")"# se añade un )
        return self.opPlace
    def doubleZero(self): #se crea la funcion de doble cero
        if len(self.opPlace) == 1 and self.opPlace[-1] == "0": #si la longitud de la variable es igual a 1 y el ultimo caracter es igual a 0
            pass # no hace nada
        elif self.opPlace[-1] == ")": #si el ultimo caracter es un )
            self.numFun(0) #añade un 0 (que a su vez pone un * antes)
        elif self.opPlace[-1] == ".": #si el ultimo caracter es un .
            self.numFun(0) #añade un 0
            self.numFun(0) #añade un 0
        elif self.opPlace[-1] == "0" and self.pulses == 1: #si el ultimo caracter es un cero y se ha puesto un punto anteriormente
            self.numFun(0) #añade un 0
            self.numFun(0) #añade un 0
        else: #de lo contrario
            self.numFun(0) #añade un 0
            self.numFun(0) #añade un 0
        return self.opPlace
    def allClear(self): #se crea la funcion de AC
        self.opPlace = "0" #la variable sera igual a 0
        self.pulses = 0 #se resetea la cantidad de veces que se pulso point a cero
        return self.opPlace
    def erase(self): # se crea la funcion erase
        if self.opPlace[-1] == ".": # si el ultimo caracter es punto
            self.opPlace = self.opPlace[:-1] # se quita el ultimo caracter de opPlace
            self.pulses = 0 # se resetea pulses a 0    
        elif len(self.opPlace) ==1: # si la longitud de opPlace es igual a 1
            self.opPlace = "0" # opPlace sera igual a 0
        else: # de lo contrario
            self.opPlace = self.opPlace[:-1] # se quita el ultimo caracter
        return self.opPlace
    def result(self): # se crea la funcion de resultado
        result = eval(self.opPlace) # la variable resultado adquiere lo que devuelva la funcion de eval acerca de opPlace
        self.opPlace = result #opPlace adquiere como valor a result
        return self.opPlace

main = Basic() #se crea la instancia de la clase
print(main.numFun(11)) # se introduce el numero 11
print(main.operator("+")) # se introduce una suma
print(main.numFun(45)) # se introduce el numero 45
print(main.result()) # se calcula el resultado

