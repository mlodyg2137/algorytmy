from math import atan2

class Graham:
    def __init__(self, points):
        self.points = points

    def orientation(self, A, B, P):
        return (B[0] - A[0])*(P[1]-A[1]) - (B[1] - A[1])*(P[0]-A[0])

    def polar_angle(self, p1, p2):
        x_span = p2[0] - p1[0]
        y_span = p2[1] - p1[1]
        return atan2(y_span, x_span)

    def distance(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def sort_by_polar_angle(self, min_point):
        return sorted(self.points, key=lambda p: (self.polar_angle(min_point, p), self.distance(min_point, p)))

    def convex_hull(self):
        if len(self.points) <= 3:
            return []

        min_point = min(self.points, key=lambda p:(p[1], p[0]))
        sorted_points = self.sort_by_polar_angle(min_point)

        stack = [sorted_points[0], sorted_points[1], sorted_points[2]]
        n = len(sorted_points)
        for i in range(3, n):
            while len(stack) > 1 and self.orientation(stack[-2], stack[-1], sorted_points[i]) <= 0:
                stack.pop()
            stack.append(sorted_points[i])

        hull = []
        while stack:
            hull.append(stack[-1])
            stack.pop()
        return hull



points = [(0, 0), (4, 4), (1, 2), (2, 3), (4, 1), (0, 4)]
graham = Graham(points)
print(graham.convex_hull())
