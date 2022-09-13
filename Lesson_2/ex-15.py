import math

x = 2.444
y = 0.869*10**-2
z = -0.13*10**3
s = 0

e = 2.7182818

print(x,y,z)

numerator1 = x**(y + 1) + e**(y - 1)
denominator1 = 1 + x * abs(y - math.tan(z))
numerator2 = ((abs(y - x)**2) / 2) - ((abs(y - x)**3) / 3)
multiplier = 1 + abs(y - x)

s = (numerator1 / denominator1) * multiplier + numerator2

print(s)

