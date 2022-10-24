array = [1,2,1,4,5,1,5,0,7]

def func():
    result = 0
    for i in range(len(array)):
        if array[i] < 0:
            continue

        if array[i] != 0:
            result+=1
        else:
            print(f"Кол-во членов в последовательности {result}")


func()