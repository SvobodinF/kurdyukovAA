def func(value):
    x = 0
    while x <= value:
        result = ""
        for i in range(0,x, 1):
            result += "[]"

        print(result)
        x += 1

func(7)