from re import A


n = 5

def func():
    s = 1
    a = 1
    while a <= n:
        s *= a 
        a += 1
    
    return s

print(func())