def func(number):
    if number < 2:
        return "Number less 2"

    if number%2 == 0:
        return 2

    i = 3

    while number%i == 0 and i*i <= number:
        i+=2

    if i*i <= number: return number

    return number


print(func(11))