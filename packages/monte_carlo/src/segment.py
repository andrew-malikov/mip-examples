from math import sqrt

from packages.monte_carlo.src.line import Line, LineBuilder
from packages.monte_carlo.src.point import Point


class Segment():
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def _get_start_point(self):
        return [min(self.a[0], self.b[0]), min(self.a[1], self.b[1])]

    def _get_end_point(self):
        return [max(self.a[0], self.b[0]), max(self.a[1], self.b[1])]

    def contain_point(self, point: Point):
        left_part = (point.x - self.a.x) * (self.b.y - self.a.y)
        right_part = (self.b.x - self.a.x) * (point.y - self.a.y)

        if not round(left_part, 5) == round(right_part, 5):
            return False

        if not min(self.a.x, self.b.x) <= point.x <= max(self.a.x, self.b.x):
            return False

        if not min(self.a.y, self.b.y) <= point.y <= max(self.a.y, self.b.y):
            return False

        return True

    def length(self):
        return sqrt((self.b.x - self.a.x)**2 + (self.b.y - self.a.y)**2)

    @staticmethod
    def is_intersects(s1, s2):
        l1, l2 = LineBuilder.from_segment(s1), LineBuilder.from_segment(s2)
        intersect = Line.get_intersect(l1, l2)

        if not intersect:
            return False

        if s1.contain_point(intersect) and s2.contain_point(intersect):
            return True

        return False
