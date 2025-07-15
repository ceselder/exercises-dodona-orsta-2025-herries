# Opgave: Tic-Tac-Toe Validator

Schrijf een functie in Python die bepaalt wie er gewonnen heeft in een Tic-Tac-Toe spel (3 op een rij). Het bord wordt voorgesteld als een tuple van drie tuples, waarbij elke tuple een rij is met drie waarden: `"X"`, `"O"` of `""` (een lege string).

De functie moet één van de volgende strings teruggeven:

- `"niemand wint"` als er geen winnaar is,
- `"X wint"` als speler X gewonnen heeft,
- `"O wint"` als speler O gewonnen heeft.

## Voorbeeld

```python
bord = (
    ("X", "O", "X"),
    ("O", "X", "O"),
    ("O", "X", "X")
)
```

Voor dit bord moet de functie `"X wint"` teruggeven.

## Functiehandtekening

```python
def bepaal_winnaar(bord)
```

### Voorbeeld 1: O wint

```python
bord = (
    ("O", "O", "O"),
    ("X", "X", ""),
    ("", "", "X")
)
bepaal_winnaar(bord)
# Dit geeft "0 wint" terug
```

### Voorbeeld 2: Niemand wint

```python
bord = (
    ("X", "O", "X"),
    ("O", "X", "O"),
    ("O", "X", "")
)
bepaal_winnaar(bord)
# Verwacht resultaat: "niemand wint"
```

### Voorbeeld 3: O wint (diagonaal)

```python
bord = (
    ("O", "X", "X"),
    ("X", "O", ""),
    ("", "", "O")
)
bepaal_winnaar(bord)
# Verwacht resultaat: "O wint"
```

### Voorbeeld 4: X wint (kolom)

```python
bord = (
    ("X", "O", ""),
    ("X", "O", "O"),
    ("X", "", "")
)
bepaal_winnaar(bord)
# Verwacht resultaat: "X wint"
```

Enz...
