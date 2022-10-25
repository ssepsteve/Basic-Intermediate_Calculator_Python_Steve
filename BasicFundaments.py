import EssentialsLib as Lib1
import math

main = Lib1.Essentials()

dict = {"add":main.Add,"+":main.Add,
"sub":main.Sub,"-":main.Sub,
"point":main.Point,".":main.Point,
"res":main.Result,#(math.pi,math.e)
"div":main.Div,"/":main.Div,
")":main.Close_Par,
"(":main.Open_Par,
"*":main.Multi,"multi":main.Multi,
"ac":main.AC,"del":main.AC,
"sqpow":main.root,"root":main.root,
"pow":main.powe,
"ln":main.ln,
"log":main.log,
"degree":main.radOrDeg,
"sin":main.sin,
"cos":main.cos,
"tan":main.tan,
"abs":main.abs,
"erase":main.erase,
"pi":main.piButton,#("π")
"euler":main.eulerButton#("e")
}





while True:
    a = str(input("Operation or num:"))
    a = a.lower()
    if a in main.numbers:
        print(main.sudoButton(int(a)))
    elif a == "res":
        print(dict.get(a)(math.pi,math.e))
    elif a == "pi":
        print(dict.get(a)("π"))
    elif a == "euler":
        print(dict.get(a)("e"))
    elif a not in dict:
        pass
    else:
        print(dict.get(a)())






'''
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
        print(main.Result(math.pi,math.e))
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
        print(Lib1.degree)
    elif a == "sin":
        main.sin()
        print(main.display)
    elif a ==  "cos":
        main.cos()
        print(main.display)
    elif a == "tan":
        main.tan()
        print(main.display)
    elif a == "abs":
        main.abs()
        print(main.display)
    elif a == "erase":
        main.erase()
        print(main.display)
    elif a == "help":
        print("Bienvenido a una simple calculadora hecha en python por Steve Espitia :) \nEste programa esta construido principalmente con palabras en ingles \npor ejemplo: Seno en español se escribe como sen() \npero en este programa decidi ponerlo como sin() \ncon el fin de que a la hora de construir el programa no me confunda con las funciones de las librerias que decidi usar \nen fin, estoy seguro de que no desplegaste help solo porque querias saber porque las palabras estan en ingles \nasi que a continuacion te mostrare cuales son las palabras que identifica este programa \nNumero(1,2,3,4,5...) = Introduce el numero que deseas poner \nSuma(+) = Introduce + o add \nResta(-) = Introduce - o sub \nMuliplicacion(x) = Introduce * o multi\nDivision(÷) = Introduce div o / \nBorrar Todo = Introduce AC o del\nBorar Individualmente = Introduce erase \nResultado = Introduce = o res\nForzar Cerrado Programa = Introduce exit\n")
        print(main.display)
print("Program End")


'''