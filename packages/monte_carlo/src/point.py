from math import sqrt


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_offset(self, x, y):
        self.x += x
        self.y += y

    def get_distance(self):
        return sqrt(self.x**2 + self.y**2)

    def is_equal(self, point):
        return self.x == point.x and self.y == point.y

    def __str__(self):
        return f"({self.x},{self.y})"
