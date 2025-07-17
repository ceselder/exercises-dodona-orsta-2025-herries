# Opgave: De Bibliotheek

In deze opgave ga je een Python-functie schrijven die een lijst van ongeordende strings (boekentitels) één voor één alfabetisch invoegt in een nieuwe lijst, zodat deze altijd gesorteerd blijft.

## Probleemstelling

Je krijgt een lijst `boeken` met ongeordende strings. Schrijf een functie `voeg_gesorteerd_toe(gesorteerde_lijst, nieuw_boek)` die een string `nieuw_boek` op de juiste alfabetische plaats invoegt in de lijst `gesorteerde_lijst`, zodat deze gesorteerd blijft.

Gebruik deze functie om alle boeken uit de lijst `boeken` in een nieuwe lijst `bibliotheek` te plaatsen, zodat `bibliotheek` altijd alfabetisch gesorteerd is.

### Voorbeeld

```python
boeken = ["Python", "Algoritmen", "Data", "Boek", "Zebra"]

bibliotheek = []
for boek in boeken:
    voeg_gesorteerd_toe(bibliotheek, boek)

print(bibliotheek)
# output: ['Algoritmen', 'Boek', 'Data', 'Python', 'Zebra']
```

## Vereisten

- Je moet de invoegpositie zelf bepalen en het boek daar invoegen.
