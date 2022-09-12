import math

x = 0.4*10**4
y = -0.875
z = -0.475*10**-3
s = 0

print(x,y,z)

numerator = abs(math.cos(x)- math.cos(y))**(1 + 2*(math.sin(y))**2)
denominator = 1 + z + (z**2 / 2) + (z**3 / 3) + (z**4 / 4)

s = numerator * denominator 

print(s)

