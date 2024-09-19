def build_subword_dictionary(text, k):
    """
    Buduje słownik wszystkich podsłów o długości k w danym tekście.

    :param text: Tekst wejściowy
    :param k: Długość podsłowa
    :return: Słownik podsłów o długości k wraz z ich pozycjami
    """
    subword_dict = {}
    n = len(text)

    for i in range(n - k + 1):
        subword = text[i:i + k]
        if subword in subword_dict:
            subword_dict[subword].append(i)
        else:
            subword_dict[subword] = [i]

    return subword_dict


# Przykład użycia
text = "abracadabra"
k = 3
subword_dict = build_subword_dictionary(text, k)
print("Słownik podsłów:", subword_dict)
pattern = "acb"
print("wystepowanie podslowa", pattern, " w tekscie:", subword_dict[pattern] if pattern in subword_dict else [])
