import math

x = -15.246
y = 4.642*10**-2
z = 21
s = 0

print(x,y,z)

numerator = math.log(y**(-math.sqrt(abs(x))))
denominator = x - y/2
multiplier = math.sin(math.atan(z))**2

s = numerator * denominator + multiplier

print(s)

