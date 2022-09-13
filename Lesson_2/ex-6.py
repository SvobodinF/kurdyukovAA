import math

x = 16.55*10**-3
y = -2.75
z = 0.15
s = 0

print(x,y,z)

numerator = math.sqrt(10 * (x**(1/3) + x**(y + 2)))
denominator = math.asin(z)**2 - abs(x-y)

s = numerator * denominator

print(s)

