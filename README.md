# 1. Struktury danych

### Struktury dla uporządkowanego multizbioru

Zbiór z elementami niemalejącymi oraz duplikatami. W Pythonie można stosować `Counter()` z biblioteki `collections`. Normalnie stosuje się drzewa BST.

Operacje:
- **Dodawanie, usuwanie, liczenie, wypisywanie** – O(n)

#### Drzewa licznikowe potęgowe (Fenwicka)

Do liczenia sumy prefiksowej (można stosować dla przedziałów). Tablica tworzona jest o rozmiarze `size+1`. Wszystko opiera się na indeksach i najmłodszym bicie (`index & -index`).

- **Dodawanie do drzewa**: dopóki `index <= size`, zwiększamy elementy o `index` o podaną wartość i zwiększamy potem `index` o `index & -index`.
- **Sprawdzanie sumy**: dopóki `index > 0`, dodajemy do wyniku wartość `tree[index]`, a następnie zmniejszamy `index` o `index & -index`.

#### Drzewa przedziałowe

Służą do liczenia sum przedziałów bądź znajdywania wartości minimalnych/maksymalnych.

- Tworzenie tablicy o wielkości `n*2`.
- **Budowanie**: Po prawej stronie drzewa dodajemy elementy z tablicy, a po lewej – wartości sum elementów.
- **Aktualizacja**: Najpierw podmieniamy wartość, a potem sumujemy odpowiednie elementy.
- **Query**: Za pomocą `left` i `right` przeszukujemy drzewo, stosując odpowiednie operacje arytmetyczne.

#### Kolejka minimów

Stosowana do dynamicznego znajdowania minimum lub maksimum o złożoności O(1). Używa się dwóch kolejek: do danych i do minimów/maksimów.

- **Dodawanie**: Dodajemy element do kolejki danych, a z kolejki minimów usuwamy elementy mniejsze od dodanego.
- **Usuwanie**: Jeśli pierwszy element z danych i minimów jest taki sam, usuwamy go.
- **Pobieranie**: Otrzymujemy minimalny element w O(1).

---

# 2. Przepływy w sieciach

- **Algorytm Forda-Fulkersona**
- **Algorytm Edmondsa-Karpa**

---

# 3. Algorytmy geometryczne

### Położenie punktu względem odcinka

Wzór na orientację punktu względem odcinka:

(x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


### Przynależność punktu do wielokąta

Sprawdzamy to, "wystrzeliwując" linię w prawo od punktu i licząc, ile razy przetnie ona boki wielokąta.

### Otoczka wypukła – Algorytm Jarvisa

Algorytm o złożoności O(n*h), gdzie n to liczba punktów, a h to liczba punktów na otoczce.

### Otoczka wypukła – Sortowanie biegunowe i algorytm Grahama

Algorytm złożoności O(n log n), bazujący na kątach polarnych punktów.

### Metoda zamiatania – Przecinanie odcinków

Algorytm do sprawdzania przecięcia odcinków na płaszczyźnie, "zamiatając" ją wirtualną linią pionową.

---

# 4. Algorytmy tekstowe

- **Algorytm naiwny** – wyszukiwanie wzorca.
- **Haszowanie i algorytm Rabina-Karpa**.
- **Algorytm KMP** – prefiksy i sufiksy.
- **Algorytm Boyera-Moore'a**.
- **Algorytm Aho-Corasick** – wyszukiwanie wzorca w tekście.
- **Algorytm Huffmana** – kodowanie.
- **Algorytm Manachera** – znajdowanie palindromów.

---

# 5. Algorytmy aproksymacyjne

### Pokrycie wierzchołkowe

Problem: Znalezienie minimalnego zbioru C⊂V, tak aby każda krawędź miała co najmniej jedno połączenie w C.

1. Tworzymy tablicę krawędzi (bez duplikatów).
2. W pętli bierzemy dowolną krawędź, przypisujemy jej punkty u i v, usuwamy zbiory krawędzi zawierające u lub v.

Współczynnik aproksymacyjny: **2**.

### Pokrycie zbioru

Problem: Znalezienie minimalnej liczby podzbiorów pokrywających zbiór U.

1. Szukamy podzbioru pokrywającego najwięcej elementów z U.
2. Usuwamy te elementy z U i podzbiór ze zbioru S.

Współczynnik aproksymacyjny: **ln(n)**.

### Problem sumy podzbioru

Problem: Znalezienie podzbioru liczb, których suma jest zbliżona do T.

1. Sortujemy zbiór malejąco.
2. Dodajemy kolejne elementy, aż `current_sum <= T`.

Współczynnik aproksymacyjny: **2**.
