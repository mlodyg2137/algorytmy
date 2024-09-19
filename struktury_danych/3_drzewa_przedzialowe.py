# Drzewa przedziałowe to struktury danych używane do operacji na przedziałach (np. zapytania o sumę, minimum lub
# maksimum na przedziale). Są one bardziej elastyczne od drzewa Fenwicka, ponieważ pozwalają na operacje na dowolnych
# przedziałach, a nie tylko prefiksowych.

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        index += self.n
        self.tree[index] = value
        while index > 0:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def query(self, left, right):
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result


# Przykład użycia
data = [1, 2, 3, 4, 5]
st = SegmentTree(data)
print("Suma na przedziale [1, 3]:", st.query(1, 4))  # Wyświetli: 9


# st.update(2, 10)
# print("Suma na przedziale [1, 3] po aktualizacji:", st.query(1, 4))  # Wyświetli: 16

