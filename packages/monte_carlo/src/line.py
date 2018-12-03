from packages.monte_carlo.src.point import Point
from packages.monte_carlo.src.multilib import sign, symbolic_sign
from math import fabs

from functools import reduce


class Line():
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def substitute(self, point):
        return self.a * point.x + self.b * point.y + self.c

    def contain_point(self, point: Point):
        return self.substitute(point) == 0

    def is_points_in_plane(self, points: list):
        if len(points) == 1:
            return True

        point_index = 0
        original_plane = 0

        for i in range(point_index, len(points)):
            plane = sign(self.substitute(points[i]))
            if plane != 0:
                original_plane = plane
                point_index = i + 1
                break

        if point_index >= len(points):
            return True

        for i in range(point_index, len(points)):
            plane = sign(self.substitute(points[i]))
            if plane != original_plane and plane != 0:
                return False
        return True

    @staticmethod
    def is_parallel(l1, l2):
        return l1.a * l2.b == l2.a * l1.b

    def __str__(self):
        signs = [
            symbolic_sign(self.a),
            symbolic_sign(self.b),
            symbolic_sign(self.c)
        ]
        values = [fabs(self.a), fabs(self.b), fabs(self.c)]
        parts = [
            f"{signs[0]}{values[0]}x\t", f"{signs[1]}{values[1]}y\t",
            f"{signs[2]}{values[2]} = 0"
        ]
        return reduce(lambda output, x: output + x, parts)


class LineBuilder():
    @staticmethod
    def from_points(p1: Point, p2: Point):
        a = p1.y - p2.y
        b = p2.x - p1.x
        c = -b * p1.y - a * p1.x
        return Line(a, b, c)

    @staticmethod
    def from_segment(segment):
        return LineBuilder.from_points(segment.a, segment.b)


class LineUtils(Line):
    def __init__(self, a, b, c):
        super(a, b, c)

    @staticmethod
    def is_intersect_with_segment(line, segment):
        line_from_segment = LineBuilder.from_segment(segment)

        intersect = Line.get_intersect(line, line_from_segment)

        if segment.contain_point(intersect):
            return True

        return False
