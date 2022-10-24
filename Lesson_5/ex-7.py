array = [1,2,1,2,3]

def func():
    result = 0

    if len(array) < 2:
            print(f"Error")
            return

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            result+=1

    print(f"Элементов больше: {result}")


func()