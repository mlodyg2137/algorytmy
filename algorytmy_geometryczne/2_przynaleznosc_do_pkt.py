def is_point_in_polygon(polygon, point):
    n = len(polygon)
    inside = False

    x, y = point
    p1x, p1y = polygon[0]

    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if min(p1y, p2y) < y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
            if p1x == p2x or x <= xinters:
                inside = not inside
        p1x, p1y = p2x, p2y

    return inside


# Przykład
polygon = [(1, 1), (5, 1), (5, 5), (1, 5)]
point = (3, 3)
print(is_point_in_polygon(polygon, point))  # Wyświetli: True (punkt wewnątrz wielokąta)
