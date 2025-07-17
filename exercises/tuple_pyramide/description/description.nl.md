## Opgave: Tuple pyramide

We willen een recursieve functie `tuple_pyramide(n, s)` schrijven die een geneste tuple-structuur opbouwt.

### Belangrijk

- Het basiselement is de string `s`.
- Er zijn in totaal `n` niveaus.
- Elke laag n structuren van het vorige niveau in een tuple.

### Voorbeelden met uitleg

Laten we de opbouw stap voor stap bekijken:

#### `tuple_pyramide(1, "x")`

- Niveau 1: gewoon `"x"` (nog geen tuple)

Resultaat:

```
"x"
```

#### `tuple_pyramide(2, "x")`

niveau 2: een 2-tuple van tuples van niveau 1

Resultaat:

```
("x", "x")
```

#### `tuple_pyramide(3, "x")`

niveau 2: een 3-tuple van tuples van niveau 2

Resultaat:

```
(("x", "x"), ("x", "x"), ("x", "x"))
```

#### `tuple_pyramide(4, "x")`

- Niveau 4: een 4-tuple van tuples van niveau 3

Resultaat:

```
((("x", "x"), ("x", "x"), ("x", "x")),(("x", "x"), ("x", "x"), ("x", "x")),(("x", "x"), ("x", "x"), ("x", "x")),(("x", "x"), ("x", "x"), ("x", "x")))
```

enz...

**Dit is een pittige oefening!**
