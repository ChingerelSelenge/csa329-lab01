import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Polyline:
    def __init__(self, points=None):
        self.points = points if points is not None else []

    def setPoints(self, points):
        self.points = points

    def getLength(self):
        length = 0.0

        for i in range(len(self.points) - 1):
            length += math.sqrt(
                (self.points[i].x - self.points[i + 1].x) ** 2
                + (self.points[i].y - self.points[i + 1].y) ** 2
            )

        return length


line = Polyline()
line.setPoints([
    Point(0, 0),
    Point(3, 4),
    Point(6, 4)
])

print("Шугамын урт:", line.getLength())