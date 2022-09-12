import math

x = 14.26
y = -1.22 
z = 3.5 * 10**-2
s = 0

print(x,y,z)

numerator = 2 * math.cos(x - 2 / 3)
denominator = 0.5 + (math.sin(y))**2
multiplier = 1 + (z**2 / (3 - (z**2/5)))

s = numerator / denominator * multiplier

print(s)
