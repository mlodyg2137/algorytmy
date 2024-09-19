# Kolejka minimów (lub maksymów) to struktura danych, która umożliwia szybkie znajdowanie wartości minimalnej (lub
# maksymalnej) w dynamicznie zmieniającym się zbiorze. Operacje, takie jak dodawanie elementu lub znajdowanie
# minimum, mogą być realizowane w czasie O(1) dzięki zastosowaniu deka (kolejki dwustronnej).

from collections import deque

class MinQueue:
    def __init__(self):
        self.queue = deque()
        self.min_deque = deque()

    def push(self, value):
        self.queue.append(value)
        while self.min_deque and self.min_deque[-1] > value:
            self.min_deque.pop()
        self.min_deque.append(value)

    def pop(self):
        if self.queue[0] == self.min_deque[0]:
            self.min_deque.popleft()
        self.queue.popleft()

    def get_min(self):
        return self.min_deque[0]

# Przykład użycia
mq = MinQueue()

mq.push(0)
mq.push(2)
mq.push(5)
mq.push(3)
mq.push(7)
mq.push(1)
mq.push(2)

print("Minimum:", mq.get_min())  # Wyświetli: 3
mq.pop()
print("Minimum po usunięciu:", mq.get_min())  # Wyświetli: 3

class minqueue:
    def __int__(self):
        self.queue = deque()
        self.min_queue = deque()

    def push(self, value):
        self.queue.append(value)
        if self.min_queue and self.min_queue[-1] > value:
            self.min_queue.pop()
        self.min_queue.append(value)

    def pop(self):
        if self.queue[0] == self.min_queue[0]:
            self.min_queue.popleft()
        self.queue.popleft()

    def get_min(self):
        return self.min_queue[0]