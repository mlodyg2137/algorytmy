import heapq
from collections import defaultdict, Counter


class Node:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char  # Znak
        self.freq = freq  # Częstotliwość
        self.left = left  # Lewy węzeł
        self.right = right  # Prawy węzeł

    def __lt__(self, other):
        return self.freq < other.freq  # Porównywanie na podstawie częstotliwości


def check_tree(root, lvl=0, pos=0):
    if root is not None:
        print(lvl, pos, root.char if root.char is not None else "SUM", root.freq)
        lvl += 1
        check_tree(root.left, lvl, 1)
        check_tree(root.right, lvl, 2)


def build_huffman_tree(text):
    """
    Buduje drzewo Huffmana na podstawie podanego tekstu.
    """
    # Zliczanie częstotliwości wystąpień znaków
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Tworzenie listy węzłów
    nodes = [Node(char, freq) for char, freq in frequency.items()]

    # Budowanie drzewa Huffmana
    while len(nodes) > 1:
        # Sortowanie węzłów według częstotliwości
        nodes = sorted(nodes, key=lambda x: x.freq)

        # Pobieranie dwóch węzłów o najmniejszych częstotliwościach
        left = nodes.pop(0)
        right = nodes.pop(0)

        # Tworzenie nowego węzła, będącego sumą dwóch najmniejszych
        merged = Node(None, left.freq + right.freq, left, right)

        # Dodanie nowego węzła do listy
        nodes.append(merged)

    check_tree(nodes[0])
    # Zwracamy korzeń drzewa
    return nodes[0]


def build_codes(node, prefix="", codebook={}):
    """
    Tworzy kody Huffmana na podstawie zbudowanego drzewa.
    """
    if node is None:
        return

    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)

    return codebook


def huffman_encoding(text):
    """
    Koduje tekst za pomocą kodów Huffmana.
    """
    root = build_huffman_tree(text)  # Budowanie drzewa Huffmana
    codebook = build_codes(root)  # Tworzenie słownika kodów
    encoded_text = "".join([codebook[char] for char in text])
    return encoded_text, codebook


def huffman_decoding(encoded_text, codebook):
    """
    Dekoduje zakodowany tekst za pomocą kodów Huffmana.
    """
    reverse_codebook = {v: k for k, v in codebook.items()}
    current_code = ""
    decoded_text = []

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_text.append(reverse_codebook[current_code])
            current_code = ""

    return "".join(decoded_text)


# Przykład użycia
text = "abracadabra"
encoded_text, codebook = huffman_encoding(text)
print("Zakodowany tekst:", encoded_text)
print("Słownik kodów:", codebook)

decoded_text = huffman_decoding(encoded_text, codebook)
print("Oryginalny tekst po dekodowaniu:", decoded_text)
