

def func():
    age = int(input("Введите возраст"))

    if age > 0 and age < 75:
        print("Правильный возраст")
    else:
        print("Неправильный возраст")
        return

    if age >= 16:
        print("Поздравляем вы поступили в ВГУИТ")
    else:    
        print("Сначала нужно окончить школу!")
        a = 16 - age
        print("вам на пары через: ", a)

        return

    name = input("Введите имя")

    if name == "Иван":
        print("ВЫ ИВАН") 
        return


func()
