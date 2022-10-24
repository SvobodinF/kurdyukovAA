
def func(value, start = 1):
    if start > value:
        print("Начальное число больше ряда")
        return

    result = 0
    a = 1
    c = 0

    for i in range(value):
        c, a = c+a,c
        
        if i >= start-1:
            result += c

    return result

print(func(int(input("Введите количество")), int(input("Введите начальное число"))))