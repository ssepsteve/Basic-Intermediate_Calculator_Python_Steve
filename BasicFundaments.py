import EssentialsLib as Lib1


main = Lib1.Essentials()


while True:
    a = str(input("Operation or num: "))
    a = a.lower()
    if a == "add" or a == "+":
        main.Add()
        print(main.text_calc)
    elif a == "pi":
        main.piButton(round(Lib1.pi,4))
        print(main.text_calc)
    elif a == "sub" or a == "-":
        main.Sub()
        print(main.text_calc)
    elif a == "point" or a == ".":
        main.Point()
        print(main.text_calc)
    elif a == "res" or a == "=" :
        main.Result()
        print(main.text_calc)
    elif a == "exit":
        break     
    elif a == "div" or a == "/":
        main.Div()
        print(main.text_calc)
    elif a == "(":
        main.Open_Par()
        print(main.text_calc)   
    elif a == ")":
        main.Close_Par()
        print(main.text_calc)   
    elif a == "multi" or a == "*":
        main.Multi()
        print(main.text_calc)
    elif a == "ac" or a == "del":
        main.AC()
        print(main.text_calc)
    elif a == "1":
        main.sudoButton(1)
        print(main.text_calc)
    elif a == "2":
        main.sudoButton(2)
        print(main.text_calc)
    elif a == "3":
        main.sudoButton(3)
        print(main.text_calc)
    elif a == "4":
        main.sudoButton(4)
        print(main.text_calc)
    elif a == "5":
        main.sudoButton(5)
        print(main.text_calc)
    elif a == "6":
        main.sudoButton(6)
        print(main.text_calc)
    elif a == "7":
        main.sudoButton(7)
        print(main.text_calc)
    elif a == "8":
        main.sudoButton(8)
        print(main.text_calc)
    elif a == "9":
        main.sudoButton(9)
        print(main.text_calc)
    elif a == "0":
        main.sudoButton(0)
        print(main.text_calc)
   
    elif a == "pow":
        main.powe()
        print(main.text_calc)

    elif a == "square":
        main.square()
        print(main.text_calc)

print("Program End")