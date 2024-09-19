def rabin_karp(T, P, d, q):
    """
    Algorytm Rabina-Karpa do wyszukiwania wzorca w tekście.

    :param T: Tekst
    :param P: Wzorzec
    :param d: Liczba znaków w alfabecie
    :param q: Liczba pierwsza używana do obliczeń modulo (duża liczba)
    :return: Lista indeksów, w których wzorzec zaczyna się w tekście
    """
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q  # wartość pomocnicza
    p = 0  # hasz wzorca
    t = 0  # hasz fragmentu tekstu
    result = []

    # Oblicz hasz wzorca i pierwszego fragmentu tekstu
    for i in range(m):
        p = (d * p + ord(P[i])) % q
        t = (d * t + ord(T[i])) % q

    # Przesuwanie wzorca wzdłuż tekstu
    for i in range(n - m + 1):
        # Jeśli hasze są równe, sprawdź dokładnie
        if p == t:
            if T[i:i + m] == P:
                result.append(i)

        # Oblicz hasz dla kolejnego fragmentu tekstu
        if i < n - m:
            t = (d * (t - ord(T[i]) * h) + ord(T[i + m])) % q
            if t < 0:
                t = t + q

    return result


# Przykład użycia
T = "abracadabra"
P = "abra"
d = 256  # Zakładamy, że mamy 256 znaków (ASCII)
q = 101  # Liczba pierwsza
result = rabin_karp(T, P, d, q)
print("Wzorzec znaleziony na pozycjach:", result)
