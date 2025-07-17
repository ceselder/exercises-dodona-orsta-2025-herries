## Opgave: Naald in een hooiberg

Schrijf een functie `vind_naald_indexes(hooiberg)` die als input een lijst van strings krijgt. De functie moet een lijst teruggeven met alle indexen waarop de string `"naald"` voorkomt in de lijst.

### Voorbeeld

```python
>>> vind_naald_indexes(["hooi", "naald", "hooi", "naald", "hooi"])
[1, 3]
```

### Gegeven

- Een lijst van strings, bijvoorbeeld: `["hooi", "naald", "hooi"]`.

### Gevraagd

- Geef een lijst terug met de indexen waar `"naald"` voorkomt.

### Tips

- Gebruik een for-lus met `enumerate()` om zowel de index als het element te krijgen.
