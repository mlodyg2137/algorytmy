def orientation(p, q, r):
    """Oblicza orientację trzech punktów.
    Zwraca:
    0 --> punkty są współliniowe
    1 --> punkty tworzą zakręt zgodnie z ruchem wskazówek zegara
    2 --> punkty tworzą zakręt przeciwnie do ruchu wskazówek zegara
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # współliniowe
    elif val > 0:
        return 1  # zgodnie z ruchem wskazówek zegara
    else:
        return 2  # przeciwnie do ruchu wskazówek zegara

def do_intersect(p1, q1, p2, q2):
    """Sprawdza, czy odcinki p1q1 i p2q2 się przecinają."""
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # Przypadek ogólny
    if o1 != o2 and o3 != o4:
        return True

    # Przypadki szczególne (gdy odcinki są współliniowe)
    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True

    return False

def on_segment(p, q, r):
    """Sprawdza, czy punkt q leży na odcinku pr."""
    if max(p[0], r[0]) >= q[0] >= min(p[0], r[0]) and \
            max(p[1], r[1]) >= q[1] >= min(p[1], r[1]):
        return True
    return False


def sweep_line(segments):
    """Znajduje wszystkie przecięcia odcinków przy użyciu metody zamiatania."""

    # Zdarzenia: początek i koniec odcinka
    events = []
    for (p1, p2) in segments:
        if p1[0] > p2[0]:  # upewnijmy się, że p1 jest lewy
            p1, p2 = p2, p1
        events.append((p1[0], 'start', p1, p2))
        events.append((p2[0], 'end', p1, p2))

    # Sortuj zdarzenia po współrzędnej x
    events.sort()

    active_segments = []  # Lista aktywnych odcinków
    intersections = []  # Lista przecięć

    for event in events:
        x, etype, p1, p2 = event
        if etype == 'start':
            # Sprawdź przecięcia z innymi aktywnymi odcinkami
            for seg in active_segments:
                if do_intersect(p1, p2, seg[0], seg[1]):
                    intersections.append((p1, p2, seg))
            # Dodaj bieżący odcinek do aktywnych
            active_segments.append((p1, p2))
        elif etype == 'end':
            # Usuń odcinek z aktywnych
            active_segments = [seg for seg in active_segments if seg != (p1, p2)]

    return intersections


# Przykład użycia
segments = [((1, 1), (5, 5)), ((1, 5), (5, 1)), ((4, 5), (5, 4))]
intersections = sweep_line(segments)
for inter in intersections:
    print("Przecięcie:", inter)