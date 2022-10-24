count = 5

def writeValues():
    values: int = []
    x = 0
    while x < count:
        values.append(int(input("Введите число")))
        x += 1

    calcul(values)

def calcul(values):
    s = 0
    for i in range(len(values)):
        s += values[i]
    
    print(f'Ответ: {s}')

writeValues()
