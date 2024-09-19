def naive_pattern_search(T, P):
    """
    Naiwny algorytm wyszukiwania wzorca w tekście.

    :param T: Tekst, w którym szukamy wzorca
    :param P: Wzorzec do wyszukania
    :return: Lista indeksów, w których wzorzec zaczyna się w tekście
    """
    n = len(T)
    m = len(P)
    result = []

    # Sprawdzaj każde możliwe przesunięcie wzorca
    for i in range(n - m + 1):
        # Sprawdzanie, czy wzorzec pasuje do bieżącego fragmentu tekstu
        match = True
        for j in range(m):
            if T[i + j] != P[j]:
                match = False
                break
        if match:
            result.append(i)

    return result


# Przykład użycia
T = "abracadabra"
P = "abra"
result = naive_pattern_search(T, P)
print("Wzorzec znaleziony na pozycjach:", result)
