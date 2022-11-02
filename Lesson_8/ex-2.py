import math

class Point:
    x = 0
    y = 0
    z = 0

    def __init__(self, x1, y1, z1):
        self.x = x1
        self.y = y1
        self.z = z1

def getDistance(startPoint: Point, endPoint: Point):
    return math.sqrt((endPoint.x - startPoint.x)**2 + (endPoint.y - startPoint.y)**2 + (endPoint.z - startPoint.z)**2)

points = []

points.append(Point(5,6,1))
points.append(Point(1,2,4))
points.append(Point(2,5,3))
points.append(Point(5,4,1))

def func():
    distance = float('inf')
    array = []

    for i in range(len(points)):
        for j in range(len(points)):
            if (i == j):
                continue

            procedularDistance = getDistance(points[i], points[j])

            if distance > procedularDistance:
                distance = procedularDistance
                array.clear()
                array.append(i)
                array.append(j)

    return f"Дистанция {distance}, Точки - {array[0]},{array[1]}"

print(func())
