from tkinter import *
import EssentialsLib as Lib1

main = Lib1.Essentials()

root = Tk()
root.title("Calculadora By Steve")
root.configure(bg="#09e6ed")
myLabel = Label(root, text = main.text_calc,width=50,height=5,background="#09e6ed")
myLabel.grid(row=0,column=0,columnspan=5)

#Funciones :Pain:
def tkSudoButton(n):
    main.sudoButton(n)
    myLabel.config(text=main.text_calc)

def tkAdd():
    main.Add()
    myLabel.config(text=main.text_calc)
def tkSub():
    main.Sub()
    myLabel.config(text=main.text_calc)
def tkDiv():
    main.Div()
    myLabel.config(text=main.text_calc)
def tkMulti():
    main.Multi()
    myLabel.config(text=main.text_calc)
def tkResult():
    main.Result()
    myLabel.config(text=main.text_calc)
def tkAC():
    main.AC()
    myLabel.config(text=main.text_calc)
def tkPoint():
    main.Point()
    myLabel.config(text=main.text_calc)
def tkOpen_Par():
    main.Open_Par()
    myLabel.config(text=main.text_calc)
def tkClose_Par():
    main.Close_Par()
    myLabel.config(text=main.text_calc)
#Botones
Button1 = Button(root, text = "1",command=lambda:tkSudoButton(1),width=10,height=5).grid(row = 1, column = 0)
Button2 = Button(root, text = "2",command=lambda:tkSudoButton(2),width=10,height=5).grid(row = 1, column = 1)
Button3 = Button(root, text = "3",command=lambda:tkSudoButton(3),width=10,height=5).grid(row = 1, column = 2)
Button4 = Button(root, text = "4",command=lambda:tkSudoButton(4),width=10,height=5).grid(row = 2, column = 0)
Button5 = Button(root, text = "5",command=lambda:tkSudoButton(5),width=10,height=5).grid(row = 2, column = 1)
Button6 = Button(root, text = "6",command=lambda:tkSudoButton(6),width=10,height=5).grid(row = 2, column = 2)
Button7 = Button(root, text = "7",command=lambda:tkSudoButton(7),width=10,height=5).grid(row = 3, column = 0)
Button8 = Button(root, text = "8",command=lambda:tkSudoButton(8),width=10,height=5).grid(row = 3, column = 1)
Button9 = Button(root, text = "9",command=lambda:tkSudoButton(9),width=10,height=5).grid(row = 3, column = 2)
Button0 = Button(root, text = "0",command=lambda:tkSudoButton(0),width=10,height=5).grid(row = 4, column = 1)

Ac = Button(root,text="AC",command=lambda: tkAC(),width=10,height=5).grid(row=1,column=3)
Del = Button(root,text="⌫",width=10,height=5) #'''Falta comando'''
Del.grid(row=2,column=3)



Res = Button(root,text="=",command=lambda: tkResult(),width=10,height=5).grid(row=4,column=3)
Add = Button(root, text = "+",command=lambda: tkAdd(),width=10,height=5).grid(row = 1, column = 4)
Sub = Button(root, text = "-",command=lambda: tkSub(),width=10,height=5).grid(row = 2, column = 4)
Div = Button(root, text = "/",command=lambda: tkDiv(),width=10,height=5).grid(row = 3, column = 4)
Multi = Button(root, text = "*",command=lambda: tkMulti(),width=10,height=5).grid(row = 4, column = 4)
Point = Button(root, text = ".",command=lambda: tkPoint(),width=10,height=5).grid(row = 4, column = 0)
Neg_Or_Pos = Button(root, text = "+/-",width=10,height=5).grid(row = 4, column = 2)
open_par = Button(root,text="(",command=lambda:tkOpen_Par())
close_par = Button(root,text=")",command=lambda:tkClose_Par())
open_par.place(x=240,y=253,width=40,height=86)
close_par.place(x=280,y=253,width=40,height=86)

root.mainloop()