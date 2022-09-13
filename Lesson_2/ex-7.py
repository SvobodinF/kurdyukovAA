import math

x = 0.1722
y = 6.33
z = 3.25*10**-4
s = 0

print(x,y,z)

f = 5 * math.atan(x)
n = (1/4 * math.acos(x)) * (x + 3 * abs(x - y) + x**2)
d = abs(x - y) * z + x**2

s = f - n / d

print(s)

