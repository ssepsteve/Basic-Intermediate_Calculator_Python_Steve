from tkinter import *
import EssentialsLib as Lib1



main = Lib1.Essentials()

root = Tk()
root.title("Python Calculator")
root.iconbitmap("calclogo.ico")
root.configure(bg="#242424")

#(NOT) FUNS

varInv = 0

def tkSudoButton(n):
    myLabel.config(text=main.sudoButton(n))
def tkDoubleZero():
    myLabel.config(text=main.doubleZero())
def tkAdd():
    myLabel.config(text=main.Add())
def tkSub():
    myLabel.config(text=main.Sub())
def tkDiv():
    myLabel.config(text=main.Div())
def tkMulti():
    myLabel.config(text=main.Multi())
def tkResult():
    myLabel.config(text=main.Result())
def tkAC():
    myLabel.config(text=main.AC())
def tkPoint():
    myLabel.config(text=main.Point())
def tkOpen_Par():
    myLabel.config(text=main.Open_Par())
def tkClose_Par():
    myLabel.config(text=main.Close_Par())
def tkErase():
    myLabel.config(text=main.erase())
def tkPi():
    myLabel.config(text=main.piButton("π"))
def tkEu():
    myLabel.config(text=main.eulerButton("e"))
def tkAbs():
    myLabel.config(text=main.abs())
def tkLog():
    myLabel.config(text=main.log())
def tkLn():
    myLabel.config(text=main.ln())
def tkSqroot():
    myLabel.config(text=main.root())
def tkPow():
    myLabel.config(text=main.powe())
def tkSin():
    myLabel.config(text=main.sin())
def tkCos():
    myLabel.config(text=main.cos())
def tkTan():
    myLabel.config(text=main.tan())
def tkSec():
    myLabel.config(text=main.sec())
def tkCsc():
    myLabel.config(text=main.csc())
def tkCot():
    myLabel.config(text=main.cot())
def tkDegree():
    myDegreeButn.config(text=main.radOrDeg())
def tkFact():
    myLabel.config(text=main.fact())
def tkRemainder():
    myLabel.config(text=main.Remainder())
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
        ButtonLog.configure(text="Log(x)",command=lambda:tkLog())
        ButtonRoot.configure(text="√(x)",command=lambda:tkSqroot())
        ButtonLn.configure(text="Ln(x)",command=lambda:tkLog())
        varInv = 0


#Fila 0

myDegreeButn = Button(root,text=main.degree,command =lambda:tkDegree(),width=10,height = 5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
myDegreeButn.grid(row=0,column=0,columnspan=1)
myLabel = Label(root,text = main.display,width=90,height = 5 ,background="#333333",foreground="#FFFFFF",anchor=E)
myLabel.grid(row=0,column=1,columnspan=8)






#Botones
#Fila 1
ButtonInv = Button(root,text="INV",command=lambda:tkINV(),width=10, height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=0)
ButtonOpenPar = Button(root,text="(",command=lambda:tkOpen_Par(),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
ButtonClosePar = Button(root,text=")",command=lambda:tkClose_Par(),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
ButtonPi = Button(root,text="π",command=lambda:tkPi(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=3)
ButtonEuler = Button(root,text="e",command=lambda:tkEu(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=2)
Button1 = Button(root,text="1",command=lambda:tkSudoButton(1),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=4)
Button2 =Button(root,text="2",command=lambda:tkSudoButton(2),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=5)
Button3 =Button(root,text="3",command=lambda:tkSudoButton(3),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=6)
ButtonAC = Button(root,text="AC",command=lambda:tkAC(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=7)
ButtonAdd = Button(root,text="+",command=lambda:tkAdd(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=8)
#Fila 2
ButtonPow = Button(root,text="^",command=lambda:tkPow(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=0)
ButtonAbs = Button(root,text="|x|",command=lambda:tkAbs(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=1)
ButtonSin = Button(root,text="Sin(x)",command=lambda:tkSin(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=2)
ButtonCos = Button(root,text="Cos(x)",command=lambda:tkCos(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=3)
Button4 = Button(root,text="4",command=lambda:tkSudoButton(4),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=4)
Button5 = Button(root,text="5",command=lambda:tkSudoButton(5),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=5)
Button6 = Button(root,text="6",command=lambda:tkSudoButton(6),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=6)
ButtonErase = Button(root,text="⌫",command=lambda:tkErase(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=7)
ButtonSub = Button(root,text="-",command=lambda:tkSub(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=8)
#Fila 3
ButtonRoot = Button(root,text="√(x)",command=lambda:tkSqroot(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
ButtonRoot.grid(row=3,column=0)
ButtonLn = Button(root,text="Ln(x)",command=lambda:tkLog(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
ButtonLn.grid(row=3,column=1)
ButtonTan = Button(root,text="Tan(x)",command=lambda:tkTan(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=2)
ButtonSec = Button(root,text="Sec(x)",command=lambda:tkSec(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=3)
Button7 = Button(root,text="7",command=lambda:tkSudoButton(7),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=4)
Button8 = Button(root,text="8",command=lambda:tkSudoButton(8),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=5)
Button9 = Button(root,text="9",command=lambda:tkSudoButton(9),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=6)
ButtonRemainder = Button(root,text="%",command=lambda:tkRemainder(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=7)
ButtonDiv = Button(root,text="÷",command=lambda:tkDiv(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=3,column=8)
#Fila 4
ButtonLog = Button(root,text="Log(x)",command=lambda:tkLog(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
ButtonLog.grid(row=4,column=0)
ButtonFact = Button(root,text="!(x)",command=lambda:tkFact(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=1)
ButtonCsc = Button(root,text="Csc(x)",command=lambda:tkCsc(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=2)
ButtonCot = Button(root,text="Cot(x)",command=lambda:tkCot(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=3)
ButtonPoint = Button(root,text=".",command=lambda:tkPoint(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=4)
Button0 = Button(root,text="0",command=lambda:tkSudoButton(0),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=5)
Button00 = Button(root,text="00",command=lambda:tkDoubleZero(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=6)
ButtonRes = Button(root,text="=",command=lambda:tkResult(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=7)
ButtonMulti = Button(root,text="X",command=lambda:tkMulti(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=8)

ButtonOpenPar.place(x=80,y=86,width=40,height=86)
ButtonClosePar.place(x=120,y=86,width=40,height=86)

root.mainloop()
