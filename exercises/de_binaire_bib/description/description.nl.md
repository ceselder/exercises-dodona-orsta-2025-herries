# Opgave: De Binaire Bibliotheek

In deze opgave ga je een Python-functie schrijven die een lijst van ongeordende strings (boekentitels) één voor één alfabetisch invoegt in een nieuwe lijst, zodat deze altijd gesorteerd blijft. Je moet hiervoor binair zoeken gebruiken om de juiste invoegpositie te vinden.

## Probleemstelling

Je krijgt een lijst `boeken` met ongeordende strings. Schrijf een functie `binaire_zoek_invoegpositie(gesorteerde_lijst, nieuw_boek)` die met behulp van binair zoeken bepaalt op welke index `nieuw_boek` moet worden ingevoegd in de lijst `gesorteerde_lijst`, zodat deze gesorteerd blijft. De functie geeft een tuple `(index, zoekstappen)` terug, waarbij `index` de juiste invoegpositie is en `zoekstappen` het aantal stappen dat de binaire zoekprocedure heeft uitgevoerd.

Gebruik deze functie om alle boeken uit de lijst `boeken` in een nieuwe lijst `bibliotheek` te plaatsen, zodat `bibliotheek` altijd alfabetisch gesorteerd is.

### Voorbeeld

```python
boeken = ["Python", "Algoritmen", "Data", "Boek", "Zebra"]

bibliotheek = []
for boek in boeken:
    index, stappen = binaire_zoek_invoegpositie(bibliotheek, boek)
    bibliotheek.insert(index, boek)
    print(f"'{boek}' ingevoegd op positie {index} na {stappen} zoekstappen.")

print(bibliotheek)
# output: ['Algoritmen', 'Boek', 'Data', 'Python', 'Zebra']
```

## Vereisten

- Je moet binair zoeken gebruiken om de invoegpositie te bepalen.
- De functie moet het aantal zoekstappen bijhouden en teruggeven.
- De functie retourneert een tuple `(index, zoekstappen)`.
- Gebruik deze functie om de boeken alfabetisch in te voegen in de bibliotheek.
