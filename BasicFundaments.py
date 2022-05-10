text_calc = "0"
result = 0
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

Button5()
Button6()
Add()
Button4()
Button8()

result = eval(text_calc)
print(result)
