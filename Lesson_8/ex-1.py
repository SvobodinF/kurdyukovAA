from unittest import result


def convert(count):
    result = {}
 
    for i in range(1,count + 1):  
        number = i
        value = ""

        while number > 0:
            value = str(number % 2) + value
            number = number // 2

        if (str(value) == str(value)[::-1]):
            result[i] = value

    return result.keys()

n = int(input("Введите число: "))

print(convert(n))