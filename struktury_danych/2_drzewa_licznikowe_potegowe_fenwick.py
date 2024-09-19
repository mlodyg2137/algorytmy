# Drzewa licznikowe, przedziałowe (Fenwicka)
#
# Drzewo Fenwicka (znane również jako drzewo potęgowe) to struktura danych, która umożliwia efektywne wykonywanie
# operacji sumy prefiksowej oraz aktualizacji elementu w tablicy. Ma ono zastosowanie m.in. w problemach związanych z
# przetwarzaniem danych dynamicznych, gdzie wymagane są częste aktualizacje oraz zapytania.

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)


# Przykład użycia
ft = FenwickTree(10)
# ft.update(3, 5)
# ft.update(3, 5)
# ft.update(5, 7)
for i in range(1, 6):
    ft.update(i, i)


class Fenwick:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size+1)

    def update(self, index, value):
        if index>0:
            while index <= self.size:
                self.tree[index] += value
                index += index & -index

    def query(self, index):
        result = 0
        if 0 < index <= self.size:
            while index > 0:
                result += self.tree[index]
                index -= index & -index
        return result

    def range_query(self, left, right):
        return self.query(right) - self.query(left-1)