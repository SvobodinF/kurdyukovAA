listType_1 = [1,1,1,"а","а","<","c","c"]
listType_2: int = [1,5,1,5,3,3,3]

def findRepeatedElements():
    result = "\nTask 1: \n"
    exceptions = ""

    for i in range(len(listType_1)):
        element = listType_1[i]
        existCount = listType_1.count(element)

        if (exceptions.count(f"{element}") == 0):
            exceptions += f"{element}"
        else:
            continue

        if existCount > 1:
            result += f"{element} "*existCount
            result += "\n"


    return result

def getOddNumbers():
    result = "\nTask 2: \n"

    exitList = []

    listType_2.sort()

    for i in range(len(listType_2)):
        if listType_2[i] % 2 != 0:
            exitList.append(listType_2[i])

    exitList.reverse()

    if len(exitList) > 0:
        result += f"{exitList}"
    else:
        result += "Нет нечетных чисел"
        
    return result

print(findRepeatedElements())
print(getOddNumbers())