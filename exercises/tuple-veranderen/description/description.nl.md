# Opgave: Aanpassen van een tuple in Python

Een tuple is een **immutable** datatype in Python, wat betekent dat je de inhoud niet direct kunt wijzigen nadat deze is aangemaakt. Soms wil je echter toch een element aanpassen. Dit kun je doen door de tuple om te zetten naar een lijst, de wijziging door te voeren, en vervolgens de lijst weer om te zetten naar een tuple.

## Opdracht

Schrijf een functie `vervang_element(tuple_invoer, index, nieuw_element)` die:

- Het element op positie `index` in `tuple_invoer` vervangt door `nieuw_element`.
- Het resultaat als een nieuwe tuple print.

## Verwachte uitvoer

```python
>>> vervang_element((1, 2, 3, 4, 5), 2, 99)
(1, 2, 99, 4, 5)
```

## Tips

- Gebruik `list()` om een tuple om te zetten naar een lijst.
- Gebruik `tuple()` om een lijst weer om te zetten naar een tuple.
