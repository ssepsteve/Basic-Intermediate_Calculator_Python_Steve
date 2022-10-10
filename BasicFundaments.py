import EssentialsLib as Lib1
import math

main = Lib1.Essentials()

#4/2+4-((root(9)+root(4)pow))
while True:
    a = str(input("Operation or num: "))
    a = a.lower()
    if a == "add" or a == "+":
        main.Add()
        print(main.display)
    elif a == "pi":
        main.piButton("π")
        print(main.display)
    elif a == "euler":
        main.eulerButton("e")
        print(main.display)
    elif a == "sub" or a == "-":
        main.Sub()
        print(main.display)
    elif a == "point" or a == ".":
        main.Point()
        print(main.display)
    elif a == "res" or a == "=" :
        main.Result(round(math.pi,4),round(math.e,4))
        print(main.display)
    elif a == "exit":
        break     
    elif a == "div" or a == "/":
        main.Div()
        print(main.display)
    elif a == "(":
        main.Open_Par()
        print(main.display)
    elif a == ")":
        main.Close_Par()
        print(main.display) 
    elif a == "multi" or a == "*":
        main.Multi()
        print(main.display)
    elif a == "ac" or a == "del":
        main.AC()
        print(main.display)
    elif a == "1":
        main.sudoButton(1)
        print(main.display)
    elif a == "2":
        main.sudoButton(2)
        print(main.display)
    elif a == "3":
        main.sudoButton(3)
        print(main.display)
    elif a == "4":
        main.sudoButton(4)
        print(main.display)
    elif a == "5":
        main.sudoButton(5)
        print(main.display)
    elif a == "6":
        main.sudoButton(6)
        print(main.display)
    elif a == "7":
        main.sudoButton(7)
        print(main.display)
    elif a == "8":
        main.sudoButton(8)
        print(main.display)
    elif a == "9":
        main.sudoButton(9)
        print(main.display)
    elif a == "0":
        main.sudoButton(0)
        print(main.display)
    elif a == "sqpow":
        main.squarePow()
        print(main.display) 
    elif a == "pow":
        main.powe()
        print(main.display)
    elif a == "square":
        main.square()
        print(main.display)
    elif a == "root":
        main.root()
        print(main.display)
    elif a == "ln":
        main.ln()
        print(main.display)
    elif a == "log":
        main.log()
        print(main.display)
    elif a == "degree":
        main.radOrDeg()
        print(main.display)
        print(main.degree)
    elif a == "sin":
        main.sin()
        print(main.display)
print("Program End")