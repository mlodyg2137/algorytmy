def set_cover_approx(universe, subsets):
    """
    Aproksymacyjny algorytm dla problemu pokrycia zbioru.

    :param universe: Zbiór elementów do pokrycia (uniwersum).
    :param subsets: Lista podzbiorów, które mogą być użyte do pokrycia.
    :return: Lista wybranych podzbiorów, które tworzą pokrycie uniwersum.
    """
    cover = []
    uncovered = set(universe)  # Zbiór niepokrytych elementów
    
    # Dopóki nie pokryto wszystkich elementów
    while uncovered:
        # Znajdź podzbiór, który pokrywa największą liczbę niepokrytych elementów
        best_subset = max(subsets, key=lambda s: len(uncovered & s))

        # Dodaj ten podzbiór do pokrycia
        cover.append(best_subset)

        # Usuń pokryte elementy z listy niepokrytych
        uncovered -= best_subset

    return cover


# Przykład użycia
universe = {1, 2, 3, 4, 5}
subsets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}]
cover = set_cover_approx(universe, subsets)
print("Pokrycie zbioru:", cover)
