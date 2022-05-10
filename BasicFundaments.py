text_calc = "0"
result = 0
def Button1():
    if text_calc == "0":
        text_calc = "1"
    else:
        text_calc = text_calc + "1"
def Button2():
    if text_calc == "0":
        text_calc = "2"
    else:
        text_calc = text_calc + "2"
def Button3(text_calc):
    if text_calc == "0":
        text_calc = "3"
    else:
        text_calc = text_calc + "3"
    return text_calc
def Button4(text_calc):
    if text_calc == "0":
        text_calc = "4"
    else:
        text_calc = text_calc + "4"
    return text_calc
def Button5():
    if text_calc == "0":
        text_calc = "5"
    else:
        text_calc = text_calc + "5"
def Button6():
    if text_calc == "0":
        text_calc = "6"
    else:
        text_calc = text_calc + "6"
def Button7():
    if text_calc == "0":
        text_calc = "7"
    else:
        text_calc = text_calc + "7"
def Button8():
    if text_calc == "0":
        text_calc = "8"
    else:
        text_calc = text_calc + "8"
def Button9():
    if text_calc == "0":
        text_calc = "6"
    else:
        text_calc = text_calc + "9"
def Button0():
    if text_calc != "0":
        text_calc = text_calc + "0"
def Add(text_calc):
    text_calc = text_calc + "+"
    return text_calc
text_calc = Button3(text_calc)
text_calc = Add(text_calc)
text_calc = Button4(text_calc)
result = eval(text_calc)
print(result)
