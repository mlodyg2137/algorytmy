# Struktury dla uporządkowanego multizbioru
#
# Multizbiór (ang. multiset) to struktura danych podobna do zbioru, z tą różnicą, że może przechowywać wiele kopii
# tego samego elementu. Struktura dla uporządkowanego multizbioru umożliwia efektywne wstawianie, usuwanie oraz
# wyszukiwanie elementów, jak również zapewnia możliwość uzyskania uporządkowanego dostępu do elementów.

from collections import Counter


class OrderedMultiset:
    def __init__(self):
        self.data = Counter()

    def insert(self, element):
        self.data[element] += 1

    def remove(self, element):
        if self.data[element] > 0:
            self.data[element] -= 1
        if self.data[element] == 0:
            del self.data[element]

    def count(self, element):
        return self.data[element]

    def elements(self):
        return sorted(self.data.elements())


# Przykład użycia
multiset = OrderedMultiset()
multiset.insert(3)
multiset.insert(1)
multiset.insert(3)
multiset.insert(2)
multiset.insert(10000)

print("Multizbiór:", multiset.elements())  # Wyświetli: [1, 2, 3, 3]
multiset.remove(3)
print("Multizbiór po usunięciu 3:", multiset.elements())  # Wyświetli: [1, 2, 3]

class OrderedMultiset2:
    def __init__(self):
        self.data = Counter()

    def insert(self, value):
        self.data[value] += 1

    def remove(self, value):
        if self.data[value] > 0:
            self.data[value] -= 1
        else:
            del self.data[value]


myset = {3, 2, 5, 1, 2, 1, 1}
print(myset)