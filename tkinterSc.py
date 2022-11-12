from tkinter import *
import EssentialsLib as Lib1
import time

start_time = time.time()
main = Lib1.Scientific()
basicBranch = Lib1.Basic()

root = Tk()
root.title("Scientific")
root.iconbitmap("calclogo.ico")
root.geometry("720x450")
root.configure(bg="#242424")







#(NOT) FUNS
varInv = 0
def tkInvLog():
    main.powe()
    main.sudoButton(1)
    myLabel.config(text=main.sudoButton(0))
def tkInvRoot():
    main.powe()
    myLabel.config(text=main.sudoButton(2))
def tkInvLn():
    main.eulerButton("e")
    myLabel.config(text=main.powe())
def tkINV():
    global varInv
    if varInv == 0:
        ButtonLog.configure(text="^10",command=lambda:tkInvLog())
        ButtonRoot.configure(text="^2",command=lambda:tkInvRoot())
        ButtonLn.configure(text="e^",command=lambda:tkInvLn())
        varInv = 1
    else:
        ButtonLog.configure(text="Log(x)",command=lambda:myLabel.config(text=main.log()))
        ButtonRoot.configure(text="√(x)",command=lambda:myLabel.config(text=main.root()))
        ButtonLn.configure(text="Ln(x)",command=lambda:myLabel.config(text=main.ln()))
        varInv = 0


#Fila 0

myDegreeButn = Button(root,text=main.degree,command =lambda:myDegreeButn.config(text=main.radOrDeg()),width=10,height = 5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
myDegreeButn.grid(row=0,column=0)
myLabel = Label(root,text = main.display,width=90,height = 5 ,background="#333333",foreground="#FFFFFF",anchor=E)
myLabel.grid(row=0,column=1,columnspan=8)






#Botones
#Fila 1
ButtonInv = Button(root,text="INV",command=lambda:tkINV(),width=10, height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=0)
ButtonOpenPar = Button(root,text="(",command=lambda:myLabel.config(text=main.Open_Par()),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
ButtonClosePar = Button(root,text=")",command=lambda:myLabel.config(text=main.Close_Par()),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
ButtonPi = Button(root,text="π",command=lambda:myLabel.config(text=main.piButton("π")),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=3)
ButtonEuler = Button(root,text="e",command=lambda:myLabel.config(text=main.eulerButton("e")),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=2)
Button1 = Button(root,text="1",command=lambda:myLabel.config(text=main.sudoButton(1)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=4)
Button2 =Button(root,text="2",command=lambda:myLabel.config(text=main.sudoButton(2)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=5)
Button3 =Button(root,text="3",command=lambda:myLabel.config(text=main.sudoButton(3)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=6)
ButtonAC = Button(root,text="AC",command=lambda:myLabel.config(text=main.AC()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=7)
ButtonAdd = Button(root,text="+",command=lambda:myLabel.config(text=main.Add()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=8)
#Fila 2
ButtonPow = Button(root,text="^",command=lambda:myLabel.config(text=main.powe()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=0)
ButtonAbs = Button(root,text="|x|",command=lambda:myLabel.config(text=main.abs()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=1)
ButtonSin = Button(root,text="Sin(x)",command=lambda:myLabel.config(text=main.sin()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=2)
ButtonCos = Button(root,text="Cos(x)",command=lambda:myLabel.config(text=main.cos()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=3)
Button4 = Button(root,text="4",command=lambda:myLabel.config(text=main.sudoButton(4)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=4)
Button5 = Button(root,text="5",command=lambda:myLabel.config(text=main.sudoButton(5)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=5)
Button6 = Button(root,text="6",command=lambda:myLabel.config(text=main.sudoButton(6)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=6)
ButtonErase = Button(root,text="⌫",command=lambda:myLabel.config(text=main.erase()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=7)
ButtonSub = Button(root,text="-",command=lambda:myLabel.config(text=main.Sub()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=8)
#Fila 3
ButtonRoot = Button(root,text="√(x)",command=lambda:myLabel.config(text=main.root()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
ButtonRoot.grid(row=3,column=0)
ButtonLn = Button(root,text="Ln(x)",command=lambda:myLabel.config(text=main.ln()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
ButtonLn.grid(row=3,column=1)
ButtonTan = Button(root,text="Tan(x)",command=lambda:myLabel.config(text=main.tan()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=2)
ButtonSec = Button(root,text="Sec(x)",command=lambda:myLabel.config(text=main.sec()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=3)
Button7 = Button(root,text="7",command=lambda:myLabel.config(text=main.sudoButton(7)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=4)
Button8 = Button(root,text="8",command=lambda:myLabel.config(text=main.sudoButton(8)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=5)
Button9 = Button(root,text="9",command=lambda:myLabel.config(text=main.sudoButton(9)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=6)
ButtonRemainder = Button(root,text="%",command=lambda:myLabel.config(text=main.Remainder()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=7)
ButtonDiv = Button(root,text="÷",command=lambda:myLabel.config(text=main.Div()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=8)
#Fila 4
ButtonLog = Button(root,text="Log(x)",command=lambda:myLabel.config(text=main.log()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
ButtonLog.grid(row=4,column=0)
ButtonFact = Button(root,text="!(x)",command=lambda:myLabel.config(text=main.fact()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=1)
ButtonCsc = Button(root,text="Csc(x)",command=lambda:myLabel.config(text=main.csc()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=2)
ButtonCot = Button(root,text="Cot(x)",command=lambda:myLabel.config(text=main.cot()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=3)
ButtonPoint = Button(root,text=".",command=lambda:myLabel.config(text=main.Point()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=4)
Button0 = Button(root,text="0",command=lambda:myLabel.config(text=main.sudoButton(0)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=5)
Button00 = Button(root,text="00",command=lambda:myLabel.config(text=main.doubleZero()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=6)
ButtonRes = Button(root,text="=",command=lambda:myLabel.config(text=main.Result()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=7)
ButtonMulti = Button(root,text="X",command=lambda:myLabel.config(text=main.Multi()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=8)

ButtonOpenPar.place(x=80,y=86,width=40,height=86)
ButtonClosePar.place(x=120,y=86,width=40,height=86)

def basicGen():
     
    basicBranch.result = 0
    basicBranch.display = "0"
    basicBranch.opPlace = "0"
    basicBranch.text_calc = "0"
    basicBranch.exce = ""
    basicBranch.pulses = 0

    root.title("Standard")
    root.geometry("400x430")
    myLabel = Label(root,text = basicBranch.display,width=56,height=5,background="#333333",foreground="#FFFFFF",anchor=E)
    myLabel.grid(row=0,column=0,columnspan=5)
    #Botones
    Button1 = Button(root, text = "1",command=lambda:myLabel.config(text=basicBranch.sudoButton(1)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 1, column = 0)
    Button2 = Button(root, text = "2",command=lambda:myLabel.config(text=basicBranch.sudoButton(2)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 1, column = 1)
    Button3 = Button(root, text = "3",command=lambda:myLabel.config(text=basicBranch.sudoButton(3)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 1, column = 2)
    Button4 = Button(root, text = "4",command=lambda:myLabel.config(text=basicBranch.sudoButton(4)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 2, column = 0)
    Button5 = Button(root, text = "5",command=lambda:myLabel.config(text=basicBranch.sudoButton(5)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 2, column = 1)
    Button6 = Button(root, text = "6",command=lambda:myLabel.config(text=basicBranch.sudoButton(6)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 2, column = 2)
    Button7 = Button(root, text = "7",command=lambda:myLabel.config(text=basicBranch.sudoButton(7)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 3, column = 0)
    Button8 = Button(root, text = "8",command=lambda:myLabel.config(text=basicBranch.sudoButton(8)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 3, column = 1)
    Button9 = Button(root, text = "9",command=lambda:myLabel.config(text=basicBranch.sudoButton(9)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 3, column = 2)
    Button0 = Button(root, text = "0",command=lambda:myLabel.config(text=basicBranch.sudoButton(0)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 1)
    Ac = Button(root,text="AC",command=lambda:myLabel.config(text=basicBranch.AC()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=3)
    Del = Button(root,text="⌫",command=lambda:myLabel.config(text=basicBranch.erase()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=3)
    Res = Button(root,text="=",command=lambda:myLabel.config(text=basicBranch.Result()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=3)
    Add = Button(root, text = "+",command=lambda:myLabel.config(text=basicBranch.Add()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 1, column = 4)
    Sub = Button(root, text = "-",command=lambda:myLabel.config(text=basicBranch.Sub()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 2, column = 4)
    Div = Button(root, text = "/",command=lambda:myLabel.config(text=basicBranch.Div()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 3, column = 4)
    Multi = Button(root, text = "*",command=lambda:myLabel.config(text=basicBranch.Multi()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 4)
    Point = Button(root, text = ".",command=lambda:myLabel.config(text=basicBranch.Point()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 0)
    DoubleZero = Button(root, text = "00",command=lambda:myLabel.config(text=basicBranch.doubleZero()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 2)
    open_par = Button(root,text="(",command=lambda:myLabel.config(text=basicBranch.Open_Par()),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
    close_par = Button(root,text=")",command=lambda:myLabel.config(text=basicBranch.Close_Par()),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
    open_par.place(x=240,y=258,width=40,height=86)
    close_par.place(x=280,y=258,width=40,height=86)

def scientificGen():
    Lib1.degree = "DEG"
    main.result = 0
    main.display = "0"
    main.opPlace = "0"
    main.text_calc = "0"
    main.exce = ""
    main.pulses = 0
    root.title("Scientific")
    root.geometry("720x430")
    
    
    #(NOT) FUNS
    global varInv
    varInv = 0
    def tkInvLog():
        main.powe()
        main.sudoButton(1)
        myLabel.config(text=main.sudoButton(0))
    def tkInvRoot():
        main.powe()
        myLabel.config(text=main.sudoButton(2))
    def tkInvLn():
        main.eulerButton("e")
        myLabel.config(text=main.powe())
    def tkINV():
        global varInv
        if varInv == 0:
            ButtonLog.configure(text="^10",command=lambda:tkInvLog())
            ButtonRoot.configure(text="^2",command=lambda:tkInvRoot())
            ButtonLn.configure(text="e^",command=lambda:tkInvLn())
            varInv = 1
        else:
            ButtonLog.configure(text="Log(x)",command=lambda:myLabel.config(text=main.log()))
            ButtonRoot.configure(text="√(x)",command=lambda:myLabel.config(text=main.root()))
            ButtonLn.configure(text="Ln(x)",command=lambda:myLabel.config(text=main.ln()))
            varInv = 0

    
    #Fila 0

    myDegreeButn = Button(root,text=main.degree,command =lambda:myDegreeButn.config(text=main.radOrDeg()),width=10,height = 5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
    myDegreeButn.grid(row=0,column=0)
    myLabel = Label(root,text = main.display,width=90,height = 5 ,background="#333333",foreground="#FFFFFF",anchor=E)
    myLabel.grid(row=0,column=1,columnspan=8)
    #Botones
    #Fila 1
    ButtonInv = Button(root,text="INV",command=lambda:tkINV(),width=10, height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=0)
    ButtonOpenPar = Button(root,text="(",command=lambda:myLabel.config(text=main.Open_Par()),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
    ButtonClosePar = Button(root,text=")",command=lambda:myLabel.config(text=main.Close_Par()),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
    ButtonPi = Button(root,text="π",command=lambda:myLabel.config(text=main.piButton("π")),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=3)
    ButtonEuler = Button(root,text="e",command=lambda:myLabel.config(text=main.eulerButton("e")),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=2)
    Button1 = Button(root,text="1",command=lambda:myLabel.config(text=main.sudoButton(1)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=4)
    Button2 =Button(root,text="2",command=lambda:myLabel.config(text=main.sudoButton(2)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=5)
    Button3 =Button(root,text="3",command=lambda:myLabel.config(text=main.sudoButton(3)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=6)
    ButtonAC = Button(root,text="AC",command=lambda:myLabel.config(text=main.AC()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=7)
    ButtonAdd = Button(root,text="+",command=lambda:myLabel.config(text=main.Add()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=8)
    #Fila 2
    ButtonPow = Button(root,text="^",command=lambda:myLabel.config(text=main.powe()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=0)
    ButtonAbs = Button(root,text="|x|",command=lambda:myLabel.config(text=main.abs()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=1)
    ButtonSin = Button(root,text="Sin(x)",command=lambda:myLabel.config(text=main.sin()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=2)
    ButtonCos = Button(root,text="Cos(x)",command=lambda:myLabel.config(text=main.cos()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=3)
    Button4 = Button(root,text="4",command=lambda:myLabel.config(text=main.sudoButton(4)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=4)
    Button5 = Button(root,text="5",command=lambda:myLabel.config(text=main.sudoButton(5)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=5)
    Button6 = Button(root,text="6",command=lambda:myLabel.config(text=main.sudoButton(6)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=6)
    ButtonErase = Button(root,text="⌫",command=lambda:myLabel.config(text=main.erase()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=7)
    ButtonSub = Button(root,text="-",command=lambda:myLabel.config(text=main.Sub()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=8)
    #Fila 3
    ButtonRoot = Button(root,text="√(x)",command=lambda:myLabel.config(text=main.root()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
    ButtonRoot.grid(row=3,column=0)
    ButtonLn = Button(root,text="Ln(x)",command=lambda:myLabel.config(text=main.ln()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
    ButtonLn.grid(row=3,column=1)
    ButtonTan = Button(root,text="Tan(x)",command=lambda:myLabel.config(text=main.tan()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=2)
    ButtonSec = Button(root,text="Sec(x)",command=lambda:myLabel.config(text=main.sec()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=3)
    Button7 = Button(root,text="7",command=lambda:myLabel.config(text=main.sudoButton(7)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=4)
    Button8 = Button(root,text="8",command=lambda:myLabel.config(text=main.sudoButton(8)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=5)
    Button9 = Button(root,text="9",command=lambda:myLabel.config(text=main.sudoButton(9)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=6)
    ButtonRemainder = Button(root,text="%",command=lambda:myLabel.config(text=main.Remainder()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=7)
    ButtonDiv = Button(root,text="÷",command=lambda:myLabel.config(text=main.Div()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=8)
    #Fila 4
    ButtonLog = Button(root,text="Log(x)",command=lambda:myLabel.config(text=main.log()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
    ButtonLog.grid(row=4,column=0)
    ButtonFact = Button(root,text="!(x)",command=lambda:myLabel.config(text=main.fact()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=1)
    ButtonCsc = Button(root,text="Csc(x)",command=lambda:myLabel.config(text=main.csc()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=2)
    ButtonCot = Button(root,text="Cot(x)",command=lambda:myLabel.config(text=main.cot()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=3)
    ButtonPoint = Button(root,text=".",command=lambda:myLabel.config(text=main.Point()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=4)
    Button0 = Button(root,text="0",command=lambda:myLabel.config(text=main.sudoButton(0)),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=5)
    Button00 = Button(root,text="00",command=lambda:myLabel.config(text=main.doubleZero()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=6)
    ButtonRes = Button(root,text="=",command=lambda:myLabel.config(text=main.Result()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=7)
    ButtonMulti = Button(root,text="X",command=lambda:myLabel.config(text=main.Multi()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=8)

    ButtonOpenPar.place(x=80,y=86,width=40,height=86)
    ButtonClosePar.place(x=120,y=86,width=40,height=86)
    


#Menu
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Mode",menu=filemenu)
filemenu.add_command(label="Standard",command=basicGen)
filemenu.add_command(label="Scientific",command=scientificGen)



end_time = time.time()
final = end_time - start_time
print(final)

root.resizable(False,False)
root.config(menu=menubar)
root.mainloop()

