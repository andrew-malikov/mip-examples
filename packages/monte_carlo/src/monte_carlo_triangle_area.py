from packages.monte_carlo.src.triangle import Triangle
from packages.monte_carlo.src.triangle_bound import TriangleBound


class MonteCarloTriangleArea:
    def __init__(self, triangle: Triangle):
        self._triangle = triangle
        self._bound = TriangleBound(triangle)

    def compute_area(self, points=1000):
        points_in_triangle = self._get_points_in_triangle(points)

        return self._bound.get_area() * points_in_triangle / points

    def _get_points_in_triangle(self, points: int) -> int:
        points_in_triangle = 0

        for i in range(0, points):
            point = self._bound.get_random_point()

            if self._triangle.is_point_inside(point):
                points_in_triangle += 1

        return points_in_triangle
