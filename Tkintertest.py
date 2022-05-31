import tkinter as tk
import EssentialsLib as Lib1

main = Lib1.Essentials()

root = tk.Tk()
root.title("Calculadora By Steve")

myLabel = tk.Label(root, text = main.text_calc).grid()


#Botones ._.

Button1 = tk.Button(root, text = "1",command=main.Button1)
Button2 = tk.Button(root, text = "2",command=main.Button2)
Button3 = tk.Button(root, text = "3",command=main.Button3)
Button4 = tk.Button(root, text = "4",command=main.Button4)
Button5 = tk.Button(root, text = "5",command=main.Button5)
Button6 = tk.Button(root, text = "6",command=main.Button6)
Button7 = tk.Button(root, text = "7",command=main.Button7)
Button8 = tk.Button(root, text = "8",command=main.Button8)
Button9 = tk.Button(root, text = "9",command=main.Button9)
Button0 = tk.Button(root, text = "0",command=main.Button0)
Add = tk.Button(root, text = "+",command=main.Add)
Sub = tk.Button(root, text = "+",command=main.Sub)



#Empaquetado

myLabel.pack()
Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
Button5.pack()
Button6.pack()
Button7.pack()
Button8.pack()
Button9.pack()
Button0.pack()




root.mainloop()