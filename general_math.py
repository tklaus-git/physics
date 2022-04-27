
import numpy as np

# point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# distance between two points

def distance(p1, p2):
    return ((p2.x -p1.x)**2 + (p2.y -p1.y)**2)**(1/2)

# p1 = Point(0,0)
# p2 = Point(0, 5)

# print(distance(p1, p2))

# forces = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
# total_force = [0, 0]

