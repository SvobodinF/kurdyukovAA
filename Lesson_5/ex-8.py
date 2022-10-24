array = [1,1,1,3,3,3,3,1,1,1,2,2,2,0,3,3,3,3,3]

def func():
    result = 0
    value = 0
    length = 0
    number = 0

    for i in range(1,len(array)):
        if array[i] == 0:
            if result < length:
                result = length
                value = number

            print(f"Больше всего элементов: {value} [{result + 1}]")
            break

        if array[i] == array[i-1]:
            length+=1
            number = array[i]
        else:
            if result < length:
                result = length
                value = number

            length = 0
            number = 0


func()