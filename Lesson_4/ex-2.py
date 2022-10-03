a = 2
b = 10

def func(x, y):
    if x > y:
        v = x
        x = y
        y = v

    while x <= y:
        if x > y:
            print(x)
            x+=1
        else:
            print(y)
            y-=1
    
func(a, b)