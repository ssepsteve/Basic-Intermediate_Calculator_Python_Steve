import os
text_calc = "0"
result = 0
class Essentials:
    
    def Button1():
        global text_calc
        if text_calc == "0":
            text_calc = "1"
        else:
            text_calc = text_calc + "1"
    def Button2():
        global text_calc
        if text_calc == "0":
            text_calc = "2"
        else:
            text_calc = text_calc + "2"
    def Button3():
        global text_calc
        if text_calc == "0":
            text_calc = "3"
        else:
            text_calc = text_calc + "3"
        
    def Button4():
        global text_calc
        if text_calc == "0":
            text_calc = "4"
        else:
            text_calc = text_calc + "4"
        
    def Button5():
        global text_calc
        if text_calc == "0":
            text_calc = "5"
        else:
            text_calc = text_calc + "5"
    def Button6():
        global text_calc
        if text_calc == "0":
            text_calc = "6"
        else:
            text_calc = text_calc + "6"
    def Button7():
        global text_calc
        if text_calc == "0":
            text_calc = "7"
        else:
            text_calc = text_calc + "7"
    def Button8():
        global text_calc
        if text_calc == "0":
            text_calc = "8"
        else:
            text_calc = text_calc + "8"
    def Button9():
        global text_calc
        if text_calc == "0":
            text_calc = "6"
        else:
            text_calc = text_calc + "9"
    def Button0():
        global text_calc
        if text_calc != "0":
            text_calc = text_calc + "0"
    def Add():
        global text_calc
        text_calc = text_calc + "+"
    def Sub():
        global text_calc
        text_calc = text_calc + "-"
    def Result():
        global text_calc, result
        result = eval(text_calc)

while True:
    a = str(input("Operation or num: "))
    a = a.lower()
    if a == "add":
        Essentials.Add()
        print(text_calc)
    elif a == "sub":
        Essentials.Sub()
        print(text_calc)
    elif a == "res":
        Essentials.Result()
        print(result)
        break
    elif a == "1":
        Essentials.Button1()
        print(text_calc)
    elif a == "2":
        Essentials.Button2()
        print(text_calc)
    elif a == "3":
        Essentials.Button3()
        print(text_calc)
    elif a == "4":
        Essentials.Button4()
        print(text_calc)
    elif a == "5":
        Essentials.Button5()
        print(text_calc)
    elif a == "6":
        Essentials.Button6()
        print(text_calc)
    elif a == "7":
        Essentials.Button7()
        print(text_calc)
    elif a == "8":
        Essentials.Button8()
        print(text_calc)
    elif a == "9":
        Essentials.Button9()
        print(text_calc)
    elif a == "0":
        Essentials.Button0()
        print(text_calc)

print("Program End")