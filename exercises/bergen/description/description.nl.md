# Opgave: Bergen sorteren

Schrijf een Python-functie die een lijst van bergen sorteert en deze afdrukt. Elke berg wordt voorgesteld als een tuple van drie elementen: `(naam, afstand, maat)`. De `maat` kan `'feet'`, `'meter'` of `'kilometer'` zijn.

## Vereisten

1. **Input:** Je krijgt drie bergen als losse tuples. Bijvoorbeeld:
   ```python
   bergen = [("Mount Everest", 8848, "meter"),("K2", 28251, "feet"),("Mont Blanc", 4.8, "kilometer")]
   ```
2. **Verwerking:** Voeg de bergen één voor één toe aan een lijst.
3. **Sorteren:** Sorteer de lijst op afstand, waarbij je alle afstanden eerst omzet naar meters.
4. **Output:** Print de gesorteerde lijst van bergen.

## Omrekeningen

- 1 kilometer = 1000 meter
- 1 foot = 0.3048 meter

## Voorbeeld

```python
sorteer_bergen(
      [("Mount Everest", 8848, "meter"),
      ("K2", 28251, "feet"),
      ("Mont Blanc", 4.8, "kilometer")]
)
```

## Verwachte output

De bergen gesorteerd van klein naar groot (op afstand in meters) worden geprint.
