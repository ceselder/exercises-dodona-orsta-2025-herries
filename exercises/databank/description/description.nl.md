# Opgave: Databank

In deze oefening werk je met een databank van video's. De databank is een **lijst van tuples** met de volgende structuur:

```python
[("videonaam", viewcount), ...]
```

Hierbij is `videonaam` een string en `viewcount` een geheel getal dat het aantal views voorstelt.

## Opdracht

Schrijf een **functie** `insert_video(databank, video)` die een nieuwe video (tuple) **invoegt op de juiste plaats** in de databank, zodat de lijst **gesorteerd blijft op viewcount** (van laag naar hoog).

Print daarna de databank in de functie

### Voorbeeld

```python
def insert_video(databank, video):
    # Jouw code hier

databank = [("Python voor Pannenkoeken", 120), ("Loops en Limonade", 300), ("Functies en Fiasco's", 500)]
insert_video(databank, ("Databanken en Donuts", 400))
print(databank)
```

**Uitvoer:**

```
[('Python voor Pannenkoeken', 120), ('Loops en Limonade', 300), ('Databanken en Donuts', 400), ('Functies en Fiasco\'s', 500)]
```

### Tips

- Gebruik geen sorteerfunctie na het invoegen.
- Zoek de juiste positie en voeg daar de nieuwe video toe.
