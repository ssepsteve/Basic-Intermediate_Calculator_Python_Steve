from tkinter import *
import EssentialsLib as Lib1

main = Lib1.Basic()

root = Tk()
root.title("Basic")
root.iconbitmap("calclogo.ico")
root.configure(bg="#242424")
myLabel = Label(root,text = main.display,width=56,height=5,background="#333333",foreground="#FFFFFF",anchor=E)
myLabel.grid(row=0,column=0,columnspan=5)

#Funciones :Pain:
def tkSudoButton(n):
    myLabel.config(text=main.sudoButton(n))

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
def tkDoubleZero():
    myLabel.config(text=main.doubleZero())

#Botones
Button1 = Button(root, text = "1",command=lambda:tkSudoButton(1),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 1, column = 0)
Button2 = Button(root, text = "2",command=lambda:tkSudoButton(2),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 1, column = 1)
Button3 = Button(root, text = "3",command=lambda:tkSudoButton(3),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 1, column = 2)
Button4 = Button(root, text = "4",command=lambda:tkSudoButton(4),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 2, column = 0)
Button5 = Button(root, text = "5",command=lambda:tkSudoButton(5),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 2, column = 1)
Button6 = Button(root, text = "6",command=lambda:tkSudoButton(6),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 2, column = 2)
Button7 = Button(root, text = "7",command=lambda:tkSudoButton(7),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 3, column = 0)
Button8 = Button(root, text = "8",command=lambda:tkSudoButton(8),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 3, column = 1)
Button9 = Button(root, text = "9",command=lambda:tkSudoButton(9),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 3, column = 2)
Button0 = Button(root, text = "0",command=lambda:tkSudoButton(0),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 1)

Ac = Button(root,text="AC",command=lambda: tkAC(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=1,column=3)
Del = Button(root,text="⌫",command=lambda:tkErase(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=3) #'''Falta comando'''




Res = Button(root,text="=",command=lambda: tkResult(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=3)
Add = Button(root, text = "+",command=lambda: tkAdd(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 1, column = 4)
Sub = Button(root, text = "-",command=lambda: tkSub(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 2, column = 4)
Div = Button(root, text = "/",command=lambda: tkDiv(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 3, column = 4)
Multi = Button(root, text = "*",command=lambda: tkMulti(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 4)
Point = Button(root, text = ".",command=lambda: tkPoint(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 0)
DoubleZero = Button(root, text = "00",command=lambda: tkDoubleZero(),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 2)

open_par = Button(root,text="(",command=lambda:tkOpen_Par(),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
close_par = Button(root,text=")",command=lambda:tkClose_Par(),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
open_par.place(x=240,y=253,width=40,height=86)
close_par.place(x=280,y=253,width=40,height=86)

root.mainloop()