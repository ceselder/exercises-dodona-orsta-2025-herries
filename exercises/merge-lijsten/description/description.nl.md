# Opgave: Samenvoegen van Gesorteerde Lijsten

Gegeven zijn twee gesorteerde lijsten van gehele getallen, `lijst1` en `lijst2`. Je taak is om een nieuwe lijst te maken waarin alle elementen van beide lijsten voorkomen, zodanig dat de nieuwe lijst ook gesorteerd is. Voeg de tweede lijst (`lijst2`) samen met de eerste lijst (`lijst1`).

## Voorbeeld

```python
lijst1 = [1, 3, 5, 7]
lijst2 = [2, 4, 6, 8]
```

Na samenvoegen:

```python
[1, 2, 3, 4, 5, 6, 7, 8]
```

## Opdracht

Schrijf een functie `merge_lijsten(lijst1, lijst2)` die twee gesorteerde lijsten samenvoegt tot één gesorteerde lijst.

### Functiehandtekening

```python
def merge_lijsten(lijst1, lijst2):
    # jouw code hier
```

### Testvoorbeeld

```python
print(merge_lijsten([1, 4, 6], [2, 3, 5]))
# Verwacht: [1, 2, 3, 4, 5, 6]
```

Let op: Gebruik geen ingebouwde sorteerfuncties zoals `sorted()` of `.sort()`. Probeer de lijsten efficiënt samen te voegen door ze element voor element te vergelijken.
