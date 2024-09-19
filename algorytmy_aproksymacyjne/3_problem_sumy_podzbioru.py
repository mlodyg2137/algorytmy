def subset_sum_approx(S, T):
    """
    Aproksymacyjny algorytm dla problemu sumy podzbioru.
    """
    S = sorted(S, reverse=True)  # Sortowanie w malejącym porządku
    current_sum = 0
    subset = []

    print(S)
    for num in S:
        if current_sum + num <= T:
            subset.append(num)
            current_sum += num

    return subset, current_sum

# Przykład
S = [3, 34, 4, 12, 5, 2]
T = 9
subset, result_sum = subset_sum_approx(S, T)
print(f"Znaleziony podzbiór: {subset}, suma: {result_sum}")
