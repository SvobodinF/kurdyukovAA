a = 2
b = 10

def func(x, y):
    while x > y:
        print(x)
        x-=1

    while x <= y:
        print(x)
        x+=1
    
func(a, b)