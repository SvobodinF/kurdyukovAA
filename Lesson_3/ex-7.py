def func(x):
    result = ""

    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        result = "Да" 
    else:
        result = "Нет" 

    return result

print(func(int(input("Введите год"))))