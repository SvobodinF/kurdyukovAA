
def func(value):
    result = 0
    a = 1
    c = 0

    for i in range(value):
        c, a = c+a,c
        
        result += c
    
    return result

print(func(int(input("Введите число"))))