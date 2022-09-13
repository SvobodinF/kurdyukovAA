import math

x = 12.3*10**-1
y = 15.4
z = 0.252*10**3
s = 0

print(x,y,z)

numerator1 = y**(x+1)
denominator1 = abs(y - 2)**(1/3) + 3
numerator2 = x + y / 2
denominator2 = 2 * abs(x + y)
multiplier = (x + 1)**(-1/math.sin(z))

s = (numerator1 / denominator1) + (numerator2 / denominator2) * multiplier

print(s)

