from traceback import format_tb


a = 21
b = 11

def func(x, y):
    if x <= y:
        print("Не верное условие Y не меньше X")
        return 


    for i in range(x,y, -1):
        if i % 2 != 0:
            print(i)
    
func(a, b)
