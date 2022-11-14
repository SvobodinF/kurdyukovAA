from random import randint
import json

def process(c, d):
    n = json.load(open("kurdyukov_artem_Y-222_vvod_ex-1.txt", "r"))
    result = []

    for i in range(len(n)):
        for j in range(len(n[i])):
            if (n[i][j] == c):
                result.append(i)

    for i in range(len(result)):
        for j in range(len(n[result[i]])):
            n[result[i]][j] *= d

    file = open("kurdyukov_artem_Y-222_vivod_ex-1.txt", "w")
    file.writelines(json.dumps(n))

def writeToFile():
    x = generator(int(input("Введите кол-вл строк")),int(input("Введите кол-вл столбцов")),int(input("Введите минимальное значение")),int(input("Введите максимальное значение")))
    
    file = open("kurdyukov_artem_Y-222_vvod_ex-1.txt", "w")
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
process(int(input("Введите искомое число")), int(input("Введите множитель")))      
print("====Complite====")
