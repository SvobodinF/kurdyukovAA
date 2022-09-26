count = 5

def writeValues():
    values: int = []
    x = 0
    while x < count:
        values.append(input("Введите число"))
        x += 1

    calcul(values)

def calcul(values):
    s = 0
    for i in values:
        s += int(values[int(i)])
    
    print(f'Ответ: {s}')

writeValues()
