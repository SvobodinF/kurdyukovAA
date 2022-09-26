a = 2
b = 11

def func(x, y):
    while x <= y:
        if x % 2 != 0:
            print(x)

        x+=1
    
func(a, b)
