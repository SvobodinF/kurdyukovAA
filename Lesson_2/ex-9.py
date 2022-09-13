import math

x = 1.825*10**2
y = 18.225
z = -3.298*10**-2
s = 0

print(x,y,z)

numerator = abs(x**(y/x) - (y/x)**(1/3))
j = y - x
denominator = math.cos(y) - (z / (y/x))
multiplier = 1 + (y - x)**2

s = numerator + j * (denominator / multiplier)

print(s)

#????????????????????????