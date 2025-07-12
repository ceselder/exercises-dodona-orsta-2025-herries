# Oefening: Plans within plans within plans...

In de vorige oefening heb je geleerd hoe je een lijst met tuples en getallen kunt ontvouwen tot één vlakke lijst. Deze keer gaan we een stap verder: nu kunnen tuples ook andere tuples bevatten, en die tuples kunnen dan ook weer tuples bevatten... op willekeurige diepte!

## Voorbeeld

```python
# Input
tuples = [7, (8, (9, 10)), (11, 12, (13, 14))]

# Output
[7, 8, 9, 10, 11, 12, 13, 14]
```

## Opdracht

1. Schrijf een functie `ontvouw_geneste_tuples(lijst_van_tuples)` die een lijst van (mogelijk geneste) tuples als parameter krijgt.
2. De functie retourneert een lijst met alle elementen uit de geneste tuples, in dezelfde volgorde.

## Hint!

Gebruik recursie om alle geneste tuples te doorlopen. Je kan nog steeds `type(current) is tuple` gebruiken om te controleren of een element een tuple is.

Dit is een pittige oefening! wees niet bang een hulpfunctie te schrijven!
