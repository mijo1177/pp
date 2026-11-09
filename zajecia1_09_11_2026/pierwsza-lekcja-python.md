# Python — zajęcia 1. Typy danych i instrukcja `if`

W zadaniach z wejściem każdą linię wczytaj osobnym wywołaniem `input()`. Wypisuj wyniki za pomocą `print()` w formacie podanym w przykładach. Każde rozwiązanie zapisz w osobnym pliku `.py`.

## Typy danych i operacje

| Typ | Przykład | Znaczenie |
|---|---|---|
| `int` | `7` | Liczba całkowita |
| `float` | `2.5` | Liczba zmiennoprzecinkowa |
| `str` | `"7"` | Tekst |
| `bool` | `True`, `False` | Wartość logiczna, np. wynik porównania |

`input()` zawsze zwraca tekst. Użyj `int()` lub `float()`, gdy chcesz wykonać obliczenia na wczytanej wartości. Funkcja `type()` pozwala sprawdzić typ wyniku. Na przykład `print(type(7 + 2.5).__name__)` wypisze `float`.

### Zadanie 1. Operacje na liczbach

Wczytaj dwie liczby całkowite. Wypisz kolejno ich sumę, różnicę (pierwsza minus druga), iloczyn i iloraz (pierwsza przez drugą). Przyjmij, że druga liczba jest różna od zera. Pod każdym wynikiem wypisz jego typ. Następnie zmień konwersję drugiej liczby z `int()` na `float()`, uruchom program na tych samych danych i sprawdź, które typy się zmieniły.

**Przykładowe wejście**

```text
8
2
```

**Przykładowe wyjście dla dwóch wartości typu `int`**

```text
10
int
6
int
16
int
4.0
float
```

### Zadanie 2. Operacje na tekście

Wczytaj dwa teksty. Wypisz wynik ich połączenia operatorem `+`, a potem wynik trzykrotnego powtórzenia pierwszego tekstu operatorem `*`. Osobno uruchom wyrażenia `"8" - "2"` oraz `"8" + 2`. Przed uruchomieniem przewidź wynik każdego wyrażenia i sprawdź, jaki błąd zgłasza Python. Następnie uzyskaj wyniki `6` i `10` po odpowiednich konwersjach.

**Przykładowe wejście**

```text
8
2
```

**Przykładowe wyjście programu**

```text
82
888
```

### Zadanie 3. Porównania i typ `bool`

Wczytaj liczbę całkowitą i liczbę zmiennoprzecinkową. Wypisz wynik porównania wczytanych tekstów za pomocą `==`, następnie wynik porównania wartości po konwersji na `int` i `float`, a na końcu wynik sprawdzenia, czy pierwsza liczba jest większa od drugiej.

**Przykładowe wejście**

```text
7
7.0
```

**Przykładowe wyjście**

```text
False
True
False
```

## Samodzielny `if` i wcięcia

`if` sprawdza warunek. Gdy warunek ma wartość `True`, Python wykonuje instrukcje w jego bloku. Gdy warunek ma wartość `False`, pomija blok i przechodzi dalej. Po warunku wpisz dwukropek. Instrukcje w bloku wsuń o cztery spacje względem linii z `if`. Operator `==` porównuje wartości, a `=` przypisuje wartość do zmiennej.

### Zadanie 4. Ten sam kod, różne wcięcia

Przepisz obie wersje do osobnych plików. Różnią się wcięciem ostatniego `print()`. Przed uruchomieniem przewidź wyjście obu programów dla wejścia `-2` i `3`. Następnie sprawdź swoje przewidywania. Wskaż, które instrukcje należą do bloku `if` w każdej wersji.

**Wersja A**

```python
liczba = int(input())
print("Start")
if liczba > 0:
    print("Liczba dodatnia")
    print("Koniec")
```

**Wersja B**

```python
liczba = int(input())
print("Start")
if liczba > 0:
    print("Liczba dodatnia")
print("Koniec")
```

**Przykładowe wejście**

```text
-2
```

**Wyjście wersji A**

```text
Start
```

**Wyjście wersji B**

```text
Start
Koniec
```

### Zadanie 5. Niezależne warunki

Wczytaj liczbę całkowitą. Wypisz `Dodatnia`, jeśli jest większa od zera, i `Parzysta`, jeśli reszta z dzielenia przez 2 wynosi zero. Użyj dwóch osobnych instrukcji `if`. Operator `%` zwraca resztę z dzielenia. Sprawdź też, co wypisze program dla `-4`, `3` i `-3`.

**Przykładowe wejście**

```text
4
```

**Przykładowe wyjście**

```text
Dodatnia
Parzysta
```

### Zadanie 6. Kalkulator

Wczytaj w trzech liniach pierwszą liczbę, operator i drugą liczbę. Liczby przekonwertuj na `float`, a operator zachowaj jako tekst. Obsłuż `+`, `-`, `*` i `/` za pomocą osobnych instrukcji `if`. Wypisz wynik tylko wybranego działania.

W bloku dzielenia użyj kolejnych instrukcji `if`, żeby wypisać wynik, gdy dzielnik jest różny od zera, albo komunikat `Nie można dzielić przez zero`, gdy dzielnik wynosi zero. Przyjmij, że użytkownik poda jeden z czterech obsługiwanych operatorów. Przetestuj każde działanie oraz dzielenie przez zero. Zapisz rozwiązanie jako `kalkulator.py`.

**Przykładowe wejście A**

```text
7.5
-
2
```

**Przykładowe wyjście A**

```text
5.5
```

**Przykładowe wejście B**

```text
8
/
0
```

**Przykładowe wyjście B**

```text
Nie można dzielić przez zero
```

## Oddanie rozwiązań

1. Umieść wszystkie pliki `.py` z zajęć w folderze `zajęcia_1`.
2. Dodaj folder `zajęcia_1` do swojego repozytorium na GitHubie i sprawdź, czy widać w nim wszystkie pliki.
3. Jeśli repozytorium jest prywatne, udostępnij je prowadzącemu. Wyślij prowadzącemu link do folderu `zajęcia_1` w repozytorium.
