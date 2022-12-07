#Блок Б задание 1

def func():
    value = int(input("введите число "))
    maxValue = value

    if value == 0:
        return maxValue

    nextValue = func()

    if maxValue < nextValue: 
        maxValue = nextValue
    
    return maxValue

print(func())