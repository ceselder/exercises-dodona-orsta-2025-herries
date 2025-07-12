# Opgave: Databank

In deze oefening werk je met een databank van video's. De databank is een **lijst van tuples** met de volgende structuur:

```python
[("videonaam", viewcount), ...]
```

Hierbij is `videonaam` een string en `viewcount` een geheel getal dat het aantal views voorstelt.

## Opdracht

Schrijf een functie `insert_video(databank, video)` die een nieuwe video (tuple) **invoegt op de juiste plaats** in de databank, zodat de lijst **gesorteerd blijft op viewcount** (van laag naar hoog).

### Voorbeeld

```python
databank = [("Intro Python", 120), ("Loops uitgelegd", 300), ("Functies", 500)]
insert_video(databank, ("Databanken", 400))
print(databank)
```

**Uitvoer:**

```
[('Intro Python', 120), ('Loops uitgelegd', 300), ('Databanken', 400), ('Functies', 500)]
```

### Tips

- Gebruik geen sorteerfunctie na het invoegen.
- Zoek de juiste positie en voeg daar de nieuwe video toe.

## Test je oplossing

Probeer je functie met verschillende invoer en controleer of de databank altijd correct gesorteerd blijft.
