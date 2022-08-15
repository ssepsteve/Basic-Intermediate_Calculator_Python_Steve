import EssentialsLib as Lib1
import math

main = Lib1.Essentials()

#4/2+4-((root(9)+root(4)pow))
while True:
    a = str(input("Operation or num: "))
    a = a.lower()
    if a == "add" or a == "+":
        main.Add()
        print(main.opPlace)
    elif a == "pi":
        main.piButton("π")
        print(main.opPlace)
    elif a == "euler":
        main.eulerButton("e")
        print(main.opPlace)
    elif a == "sub" or a == "-":
        main.Sub()
        print(main.opPlace)
    elif a == "point" or a == ".":
        main.Point()
        print(main.opPlace)
    elif a == "res" or a == "=" :
        main.Result(round(math.pi,4),round(math.e,4))
        print(main.opPlace)
    elif a == "exit":
        break     
    elif a == "div" or a == "/":
        main.Div()
        print(main.opPlace)
    elif a == "(":
        main.Open_Par()
        print(main.opPlace)
    elif a == ")":
        main.Close_Par()
        print(main.opPlace) 
    elif a == "multi" or a == "*":
        main.Multi()
        print(main.opPlace)
    elif a == "ac" or a == "del":
        main.AC()
        print(main.opPlace)
    elif a == "1":
        main.sudoButton(1)
        print(main.opPlace)
    elif a == "2":
        main.sudoButton(2)
        print(main.opPlace)
    elif a == "3":
        main.sudoButton(3)
        print(main.opPlace)
    elif a == "4":
        main.sudoButton(4)
        print(main.opPlace)
    elif a == "5":
        main.sudoButton(5)
        print(main.opPlace)
    elif a == "6":
        main.sudoButton(6)
        print(main.opPlace)
    elif a == "7":
        main.sudoButton(7)
        print(main.opPlace)
    elif a == "8":
        main.sudoButton(8)
        print(main.opPlace)
    elif a == "9":
        main.sudoButton(9)
        print(main.opPlace)
    elif a == "0":
        main.sudoButton(0)
        print(main.opPlace) 
    elif a == "pow":
        main.powe()
        print(main.opPlace)
    elif a == "square":
        main.square()
        print(main.opPlace)
    elif a == "root":
        main.root()
        print(main.opPlace)
print("Program End")