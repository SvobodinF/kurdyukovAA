def func():
    n = 3
    a = 0
    s = 0

    while a <= n:
        s += a**3
        a+=1

    return s

print(func())
