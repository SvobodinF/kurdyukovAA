#Блок А задание 4

def func(number):
    y = number//10
    x = number - (y * 10)

    if y == 0:
        return x

    x += func(y)
    
    return x

print(func(int(input("Введите число"))))