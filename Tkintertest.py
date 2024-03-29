from tkinter import *
import EssentialsLib as Lib1
import time

start_time = time.time()

basicBranch = Lib1.Basic()

root = Tk()
root.title("Basic")
root.iconbitmap("calclogo.ico")
root.configure(bg="#242424")
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
Del = Button(root,text="⌫",command=lambda:myLabel.config(text=basicBranch.erase()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=2,column=3) #'''Falta comando'''




Res = Button(root,text="=",command=lambda:myLabel.config(text=basicBranch.Result()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row=4,column=3)
Add = Button(root, text = "+",command=lambda:myLabel.config(text=basicBranch.Add()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 1, column = 4)
Sub = Button(root, text = "-",command=lambda:myLabel.config(text=basicBranch.Sub()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 2, column = 4)
Div = Button(root, text = "/",command=lambda:myLabel.config(text=basicBranch.Div()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 3, column = 4)
Multi = Button(root, text = "*",command=lambda:myLabel.config(text=basicBranch.Multi()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 4)
Point = Button(root, text = ".",command=lambda:myLabel.config(text=basicBranch.Point()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 0)
DoubleZero = Button(root, text = "00",command=lambda:myLabel.config(text=basicBranch.doubleZero()),width=10,height=5,background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF").grid(row = 4, column = 2)

open_par = Button(root,text="(",command=lambda:myLabel.config(text=basicBranch.Open_Par()),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
close_par = Button(root,text=")",command=lambda:myLabel.config(text=basicBranch.Close_Par()),background="#3a3a3a",foreground="#FFFFFF",activebackground="#3a3a3a",activeforeground="#FFFFFF")
open_par.place(x=240,y=253,width=40,height=86)
close_par.place(x=280,y=253,width=40,height=86)

end_time = time.time()
final = end_time - start_time
print(final)


root.mainloop()