def bad_character_heuristic(P):
    """
    Buduje tablicę złego znaku dla wzorca.
    """
    bad_char = [-1] * 256  # Zakładamy, że mamy 256 znaków (ASCII)

    for i in range(len(P)):
        bad_char[ord(P[i])] = i

    return bad_char


def boyer_moore_search(T, P):
    """
    Algorytm Boyera-Moore'a do wyszukiwania wzorca w tekście.

    :param T: Tekst
    :param P: Wzorzec
    :return: Lista indeksów, gdzie wzorzec występuje w tekście
    """
    m = len(P)
    n = len(T)
    bad_char = bad_character_heuristic(P)
    result = []

    s = 0  # s to przesunięcie wzorca względem tekstu
    while s <= n - m:
        j = m - 1

        # Porównujemy wzorzec z tekstem od prawej do lewej
        while j >= 0 and P[j] == T[s + j]:
            j -= 1

        if j < 0:
            result.append(s)
            s += (m - bad_char[ord(T[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(T[s + j])])

    return result


# Przykład użycia
T = "ABAAABCDABC"
P = "ABC"
result = boyer_moore_search(T, P)
print("Wzorzec znaleziony na pozycjach:", result)
