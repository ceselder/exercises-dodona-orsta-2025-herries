# Opgave: Groeperen op basis van verschil

Gegeven een gesorteerde lijst van gehele getallen, schrijf een Python-functie die deze lijst opsplitst in groepen waarbij het verschil tussen opeenvolgende getallen **exact gelijk is**. Elke groep bevat dus getallen die eenzelfde sprong maken.

## Voorbeeld

```python
# Input
getallen = [2, 4, 6, 9, 12, 15, 18]

# Output
groepen = groepeer_op_verschil(getallen)
print(groepen) # [[2, 4, 6], [9, 12, 15, 18]]
```

In dit voorbeeld is het verschil tussen 2, 4 en 6 telkens 2, en tussen 9, 12, 15, 18 telkens 3.

## Vereisten

- Implementeer een functie `groepeer_op_verschil(lijst)` die de gesorteerde lijst als parameter krijgt en een lijst van groepen retourneert.
- Elke groep bevat minstens twee getallen.
- Gebruik Python-lijstoperaties en slicing waar mogelijk.

Veel succes!
