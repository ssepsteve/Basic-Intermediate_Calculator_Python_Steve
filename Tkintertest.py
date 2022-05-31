from tkinter import *
import EssentialsLib as Lib1

main = Lib1.Essentials()

root = Tk()
root.title("Calculadora By Steve")

myLabel = Label(root, text = main.text_calc,width=50)
myLabel.grid(row=0,column=0,columnspan=5)

#Botones ._.
def tkButton1():
    main.Button1()
    myLabel.config(text=main.text_calc)


Button1 = Button(root, text = "1",command=lambda:tkButton1()).grid(row = 1, column = 0)
Button2 = Button(root, text = "2",command=main.Button2).grid(row = 1, column = 1)
Button3 = Button(root, text = "3",command=main.Button3).grid(row = 1, column = 2)
Button4 = Button(root, text = "4",command=main.Button4).grid(row = 2, column = 0)
Button5 = Button(root, text = "5",command=main.Button5).grid(row = 2, column = 1)
Button6 = Button(root, text = "6",command=main.Button6).grid(row = 2, column = 2)
Button7 = Button(root, text = "7",command=main.Button7).grid(row = 3, column = 0)
Button8 = Button(root, text = "8",command=main.Button8).grid(row = 3, column = 1)
Button9 = Button(root, text = "9",command=main.Button9).grid(row = 3, column = 2)
Button0 = Button(root, text = "0",command=main.Button0).grid(row = 4, column = 1)

Ac = Button(root,text="AC",command=main.AC).grid(row=1,column=3)
Del = Button(root,text="↼").grid(row=2,column=3)
#open_par = Button(root,text="(",command=main.Open_Par).grid(row=3,column=3)
#close_par = Button(root,text=")",command=main.Close_Par).grid(row=3,column=3)
Res = Button(root,text="=",command=main.Result).grid(row=4,column=3)
Add = Button(root, text = "+",command=main.Add).grid(row = 1, column = 4)
Sub = Button(root, text = "-",command=main.Sub).grid(row = 2, column = 4)
Sub = Button(root, text = "/",command=main.Div).grid(row = 3, column = 4)
Sub = Button(root, text = "*",command=main.Multi).grid(row = 4, column = 4)



root.mainloop()