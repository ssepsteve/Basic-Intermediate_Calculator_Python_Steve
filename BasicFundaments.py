import EssentialsLib as Lib1


main = Lib1.Essentials()

while True:
    a = str(input("Operation or num: "))
    a = a.lower()
    if a == "add" or a == "+":
        main.Add()
        print(main.text_calc)
    elif a == "sub" or a == "-":
        main.Sub()
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
    elif a == "AC" or a == "del":
        main.AC()
        print(main.text_calc)
    elif a == "1":
        main.Button1()
        print(main.text_calc)
    elif a == "2":
        main.Button2()
        print(main.text_calc)
    elif a == "3":
        main.Button3()
        print(main.text_calc)
    elif a == "4":
        main.Button4()
        print(main.text_calc)
    elif a == "5":
        main.Button5()
        print(main.text_calc)
    elif a == "6":
        main.Button6()
        print(main.text_calc)
    elif a == "7":
        main.Button7()
        print(main.text_calc)
    elif a == "8":
        main.Button8()
        print(main.text_calc)
    elif a == "9":
        main.Button9()
        print(main.text_calc)
    elif a == "0":
        main.Button0()
        print(main.text_calc)

print("Program End")