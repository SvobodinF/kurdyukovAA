from unittest import result


values = [5, 3, 10]

def GetMin(array):
    result = array[0]

    for i in range(len(array)):
        if (array[i] < result):
            result = array[i]
    
    return result


print(GetMin(values))
