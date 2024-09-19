def orientation(p, q, r):
    """Oblicza orientację trzech punktów (p, q, r)."""
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])


def jarvis_march(points):
    """Znajduje otoczkę wypukłą dla zbioru punktów."""
    if len(points) < 3:
        return points  # Otoczka wypukła nie istnieje dla mniej niż 3 punktów.

    # Znajdujemy najbardziej lewy punkt
    leftmost = min(points, key=lambda p: p[0])

    # Lista do przechowywania punktów na otoczce wypukłej
    hull = []
    point_on_hull = leftmost

    while True:
        # Dodajemy bieżący punkt do otoczki wypukłej
        hull.append(point_on_hull)

        # Wybieramy dowolny punkt jako kandydat do bycia kolejnym punktem na otoczce
        next_point = points[0]

        for candidate in points:
            # Jeżeli next_point jest tym samym co point_on_hull, lub kandydat leży po lewej stronie
            if next_point == point_on_hull or orientation(point_on_hull, next_point, candidate) > 0:
                next_point = candidate

        # Przechodzimy do następnego punktu na otoczce
        point_on_hull = next_point

        # Kończymy, jeśli wróciliśmy do punktu początkowego
        if point_on_hull == leftmost:
            break

    return hull


# Przykład użycia
points = [(0, 0), (4, 4), (1, 2), (2, 3), (4, 1), (0, 4)]
hull = jarvis_march(points)
print("Otoczka wypukła:", hull)
hull = jarvis_march(points)
print("Otoczka wypukła:", hull)
