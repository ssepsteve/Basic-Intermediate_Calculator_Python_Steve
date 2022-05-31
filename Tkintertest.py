from tkinter import *
import EssentialsLib as Lib1

main = Lib1.Essentials()

root = Tk()
root.title("Calculadora By Steve")

myLabel = Label(root, text = main.text_calc,width=50)
myLabel.grid(row=0,column=0,columnspan=5)

#Funciones :Pain:
def tkButton1():
    main.Button1()
    myLabel.config(text=main.text_calc)
def tkButton1():
    main.Button1()
    myLabel.config(text=main.text_calc)
def tkButton2():
    main.Button2()
    myLabel.config(text=main.text_calc)
def tkButton3():
    main.Button3()
    myLabel.config(text=main.text_calc)
def tkButton4():
    main.Button4()
    myLabel.config(text=main.text_calc)
def tkButton5():
    main.Button5()
    myLabel.config(text=main.text_calc)
def tkButton6():
    main.Button6()
    myLabel.config(text=main.text_calc)
def tkButton7():
    main.Button7()
    myLabel.config(text=main.text_calc)
def tkButton8():
    main.Button8()
    myLabel.config(text=main.text_calc)
def tkButton9():
    main.Button9()
    myLabel.config(text=main.text_calc)
def tkButton0():
    main.Button0()
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


#Botones
Button1 = Button(root, text = "1",command=lambda:tkButton1()).grid(row = 1, column = 0)
Button2 = Button(root, text = "2",command=lambda:tkButton2()).grid(row = 1, column = 1)
Button3 = Button(root, text = "3",command=lambda:tkButton3()).grid(row = 1, column = 2)
Button4 = Button(root, text = "4",command=lambda:tkButton4()).grid(row = 2, column = 0)
Button5 = Button(root, text = "5",command=lambda:tkButton5()).grid(row = 2, column = 1)
Button6 = Button(root, text = "6",command=lambda:tkButton6()).grid(row = 2, column = 2)
Button7 = Button(root, text = "7",command=lambda:tkButton7()).grid(row = 3, column = 0)
Button8 = Button(root, text = "8",command=lambda:tkButton8()).grid(row = 3, column = 1)
Button9 = Button(root, text = "9",command=lambda:tkButton9()).grid(row = 3, column = 2)
Button0 = Button(root, text = "0",command=lambda:tkButton0()).grid(row = 4, column = 1)

Ac = Button(root,text="AC",command=lambda: tkAC()).grid(row=1,column=3)
Del = Button(root,text="↼").grid(row=2,column=3)
#open_par = Button(root,text="(",command=main.Open_Par).grid(row=3,column=3)
#close_par = Button(root,text=")",command=main.Close_Par).grid(row=3,column=3)
Res = Button(root,text="=",command=lambda: tkResult()).grid(row=4,column=3)
Add = Button(root, text = "+",command=lambda: tkAdd()).grid(row = 1, column = 4)
Sub = Button(root, text = "-",command=lambda: tkSub()).grid(row = 2, column = 4)
Div = Button(root, text = "/",command=lambda: tkDiv()).grid(row = 3, column = 4)
Multi = Button(root, text = "*",command=lambda: tkMulti()).grid(row = 4, column = 4)



root.mainloop()