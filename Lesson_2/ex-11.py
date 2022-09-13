from cmath import cos
import math

x = 6.251
y = 0.827
z = 25.001
s = 0

e = 2.7182818

print(x,y,z)

numerator = y**(abs(x)**(1/3))
denominator = cos(y)**3
multiplier = abs(x-y) * (1 + (math.sin(z)**2) / math.sqrt(x + y))
j = e**(abs(x - y)) + x / 2

s = numerator + denominator * multiplier / j

print(s)

