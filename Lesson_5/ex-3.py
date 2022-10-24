n = 2139

def func():
    degree = 1
    value = 1
    for i in range(1, n):
        value *= 2
        degree = i

        if (value > n):
            return f"Степень:{value//2}, Показатель: {degree - 1}"
            


print(func())