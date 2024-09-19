def compute_prefix_function(P):
    """
    Oblicza tablicę prefiksów dla wzorca.
    :param P: Wzorzec
    :return: Tablica prefiksów
    """
    m = len(P)
    pi = [0] * m
    k = 0

    for i in range(1, m):
        while k > 0 and P[k] != P[i]:
            k = pi[k - 1]
        if P[k] == P[i]:
            k += 1
        pi[i] = k

    return pi


def kmp_search(T, P):
    """
    Algorytm KMP do wyszukiwania wzorca w tekście.

    :param T: Tekst
    :param P: Wzorzec
    :return: Lista indeksów, gdzie wzorzec występuje w tekście
    """
    n = len(T)
    m = len(P)
    pi = compute_prefix_function(P)
    result = []
    k = 0  # Licznik dopasowanych znaków

    for i in range(n):
        while k > 0 and P[k] != T[i]:
            k = pi[k - 1]
        if P[k] == T[i]:
            k += 1
        if k == m:
            result.append(i - m + 1)
            k = pi[k - 1]

    return result


# Przykład użycia
T = "abababdcabababd"
P = "ababd"
result = kmp_search(T, P)
print("Wzorzec znaleziony na pozycjach:", result)
