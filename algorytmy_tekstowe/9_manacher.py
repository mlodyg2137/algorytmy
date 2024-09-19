def preprocess_string(s):
    """
    Przekształca ciąg, dodając sztuczne znaki (#), aby poradzić sobie z parzystymi i nieparzystymi palindromami.
    """
    if not s:
        return "^$"
    result = "^"  # Znak startowy, który pomaga uniknąć problemów z granicami
    for char in s:
        result += "#" + char
    result += "#$"  # Znak końcowy
    return result


def manacher(s):
    """
    Algorytm Manachera do znajdowania najdłuższego palindromu w czasie O(n).

    :param s: Oryginalny ciąg znaków
    :return: Najdłuższy palindromiczny podciąg
    """
    # Przekształcamy ciąg, aby łatwo radzić sobie z parzystymi i nieparzystymi palindromami
    T = preprocess_string(s)
    n = len(T)
    P = [0] * n  # Tablica długości palindromów dla przekształconego ciągu
    center = 0
    right = 0

    # Algorytm Manachera
    for i in range(1, n - 1):
        mirror = 2 * center - i  # Pozycja lustrzana w stosunku do bieżącego centrum

        if i < right:
            P[i] = min(right - i, P[mirror])  # Używamy symetrii palindromu, aby przyspieszyć obliczenia

        # Próbujemy rozszerzyć palindrom wokół i
        while T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # Aktualizacja centrum i prawej granicy, jeśli udało się znaleźć większy palindrom
        if i + P[i] > right:
            center = i
            right = i + P[i]

    # Znalezienie najdłuższego palindromu
    max_len = 0
    center_index = 0
    for i in range(1, n - 1):
        if P[i] > max_len:
            max_len = P[i]
            center_index = i

    # Odtworzenie oryginalnego palindromu
    start = (center_index - max_len) // 2  # Wyznaczamy początek w oryginalnym ciągu
    return s[start:start + max_len]


# Przykład użycia
s = "abcbabcbabcba"
s2 = "acbbcacaaabbbaaacb"
longest_palindrome = manacher(s2)
print("Najdłuższy palindrom:", longest_palindrome)
