from re import X


n = 50

def func():
    if n <= 0:
        return

    for i in range(1,n):
        x = i**2

        if x <= n:
            print(x)

func()