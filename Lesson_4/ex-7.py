def func(n):
    a = 1
    s = 0

    while a <= n:
        x = 1
        for i in range(1,n,1):
            x *= i
        

        s += x
        a += 1 

    return s

print(func(5))
            

