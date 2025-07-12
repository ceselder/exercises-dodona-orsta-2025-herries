# Oefening: Tuples ontvouwen

Gegeven een lijst van Python tuples en getallen, schrijf een functie die deze lijst "ontvouwt" tot een enkele lijst met alle elementen uit de tuples. **let op! er kunnen dus ook getallen tussen zitten die helemaal geen tuple zijn (zie voorbeeld)**

## Voorbeeld

```python
# Input
tuples = [7, (8, 9), (10, 11, 12)]

# Output
[7, 8, 9, 10, 11, 12]
```

## Opdracht

1. Schrijf een functie `ontvouw_tuples(lijst_van_tuples)` die een lijst van tuples als parameter krijgt.
2. De functie retourneert een lijst met alle elementen uit de tuples, in dezelfde volgorde.

## Hint!

Je kan op de volgende manier checken of iets een tuple is of niet:

```python
if type(current) is tuple
```
