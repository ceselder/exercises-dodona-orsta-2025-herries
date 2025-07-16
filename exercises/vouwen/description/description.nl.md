# Opgave: Groepeer een lijst in dynamische tuples

Schrijf een Python-functie `groepeer_in_tuples(lst, n)` die een lijst van waarden omzet naar een lijst van tuples, waarbij elke tuple `n` opeenvolgende elementen uit de oorspronkelijke lijst bevat. Als het aantal elementen in de lijst niet deelbaar is door `n`, wordt het laatste incomplete groepje genegeerd.

## Voorbeeld

```python
>>> groepeer_in_tuples([1, 2, 3, 4, 5, 6], 3)
[(1, 2, 3), (4, 5, 6)]

>>> groepeer_in_tuples(['a', 'b', 'c', 'd', 'e'], 2)
[('a', 'b'), ('c', 'd')]

>>> groepeer_in_tuples([10, 20, 30, 40, 50], 4)
[(10, 20, 30, 40)]
```

Experimenteer met verschillende waarden voor `n` om te zien hoe de lijst wordt gegroepeerd!
