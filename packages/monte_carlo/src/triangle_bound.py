from packages.monte_carlo.src.triangle import Triangle
from packages.monte_carlo.src.point import Point

from packages.random.src.uniform import UniformRandom


class TriangleBound:
    def __init__(self, triangle: Triangle):
        self.left = self._find_left_bound(triangle.points)
        self.right = self._find_right_bound(triangle.points)
        self.up = self._find_up_bound(triangle.points)
        self.down = self._find_down_bound(triangle.points)
        self.random = UniformRandom()

    def _find_left_bound(self, points: [Point]) -> float:
        bound = points[0].x

        for i in range(0, len(points)):
            if points[i].x < bound:
                bound = points[i].x

        return bound

    def _find_right_bound(self, points: [Point]) -> float:
        bound = points[0].x

        for i in range(0, len(points)):
            if points[i].x > bound:
                bound = points[i].x

        return bound

    def _find_up_bound(self, points: [Point]) -> float:
        bound = points[0].y

        for i in range(0, len(points)):
            if points[i].y > bound:
                bound = points[i].y

        return bound

    def _find_down_bound(self, points: [Point]) -> float:
        bound = points[0].y

        for i in range(0, len(points)):
            if points[i].y < bound:
                bound = points[i].y

        return bound

    def get_random_point(self) -> Point:
        return Point(
            self.random.next([self.left, self.right]),
            self.random.next([self.down, self.up]))

    def get_area(self) -> float:
        return (self.right - self.left) * (self.up - self.down)
