def vertex_cover_approx(graph):
    """
    Aproksymacyjny algorytm dla problemu pokrycia wierzchołkowego.
    Graf reprezentowany jako słownik sąsiedztwa.
    Zwraca zbiór wierzchołków tworzących pokrycie wierzchołkowe.
    """
    cover = set()  # Zbiór pokrycia wierzchołkowego
    edges = set()  # Zbiór niepokrytych krawędzi

    # Utwórz listę krawędzi na podstawie grafu
    for u in graph:
        for v in graph[u]:
            if u < v:  # Dodajemy tylko jedną wersję każdej krawędzi
                edges.add((u, v))
    print("all edges:", edges)
    # Dopóki są niepokryte krawędzie
    while edges:
        # Wybierz dowolną niepokrytą krawędź (u, v)
        (u, v) = edges.pop()

        # Dodaj oba wierzchołki do pokrycia
        cover.add(u)
        cover.add(v)
        print("edges before: ", edges)
        # Usuń wszystkie krawędzie incydentne do u i v
        edges = {(x, y) for (x, y) in edges if x != u and x != v and y != u and y != v}
        print("edges after: ", edges)

    return cover


# Przykładowy graf reprezentowany jako słownik sąsiedztwa
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 4],
    3: [2, 4],
    4: [2, 3]
}

cover = vertex_cover_approx(graph)
print("Pokrycie wierzchołkowe:", cover)
