array = [1,1,1,4,0,5,5,0]

def func():
    result = 0
    for i in range(len(array)):
        if array[0] == 0:
            print(f"Error")
            break

        if array[i] != 0:
            result+=array[i]
        else:
            print(f"Среднее последовательности {result / (i)}")
            break


func()