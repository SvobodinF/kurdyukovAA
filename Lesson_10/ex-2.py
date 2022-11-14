from random import randint
import json 

def process():
    n = json.load(open("kurdyukov_artem_Y-222_vvod_ex-2.txt", "r"))
    maxSum = 0
    line = -1

    for i in range(len(n)):
        lineSum = 0
        for j in range(len(n[i])):
            if line == i:
                continue

            if n[i][j] % 2 == 0:
                line = i
            else:
                lineSum += my_abs(n[i][j])

        if lineSum > maxSum:
            maxSum = lineSum    
            line = i

    file = open("kurdyukov_artem_Y-222_vivod_ex-2.txt", "w")
    file.writelines(f"{line},{maxSum}")

def my_abs(a):
    return a if a > 0 else -a

def writeToFile():
    x = generator(int(input("Введите кол-вл строк")),int(input("Введите кол-вл столбцов")),int(input("Введите минимальное значение")),int(input("Введите максимальное значение")))
    
    file = open("kurdyukov_artem_Y-222_vvod_ex-2.txt", "w")
    file.writelines(json.dumps(x))

def generator(row, column, maxValue, minValue):
    rowA = []
    for i in range(row):
        columnA = []
        for f in range(column):
            columnA.append(randint(maxValue,minValue))
            
        rowA.append(columnA)

    return rowA

writeToFile()
process()