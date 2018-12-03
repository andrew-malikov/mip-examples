from enum import Enum

from packages.monte_carlo.src.line import LineBuilder
from packages.monte_carlo.src.segment import Segment


class PointOrientation(Enum):
    INNER = 'inner'
    OUTER = 'outer'
    ON_POLYGON = 'on_polygon'


class Triangle():
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]
        self.sides = [
            Segment(p1, p2).length(),
            Segment(p2, p3).length(),
            Segment(p3, p1).length()
        ]

    def get_point_orientation(self, point) -> PointOrientation:
        lines = self.get_lines()

        for i in range(0, len(lines)):
            if not lines[i].is_points_in_plane([self.get_point(i + 2), point]):
                return PointOrientation.OUTER

        for line in lines:
            if line.contain_point(point):
                return PointOrientation.ON_POLYGON

        return PointOrientation.INNER

    def is_point_inside(self, point) -> bool:
        position = self.get_point_orientation(point)
        return position == position.INNER or position == position.ON_POLYGON

    def get_lines(self):
        lines = []
        for i in range(0, len(self.points)):
            line = LineBuilder.from_points(
                self.points[i], self.points[(i + 1) % len(self.points)])
            lines.append(line)
        return lines

    def get_point(self, offset):
        return self.points[offset % len(self.points)]
