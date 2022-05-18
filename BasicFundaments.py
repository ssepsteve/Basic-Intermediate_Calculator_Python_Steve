import os
import EssentialsLib as Lib1


main = Lib1.Essentials()

while True:
    a = str(input("Operation or num: "))
    a = a.lower()
    if a == "add":
        main.Add()
        print(main.text_calc)
    elif a == "sub":
        main.Sub()
        print(main.text_calc)
    elif a == "res":
        main.Result()
        print(main.result)
        break
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