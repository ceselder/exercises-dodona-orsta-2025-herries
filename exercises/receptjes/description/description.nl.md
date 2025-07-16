# Opgave: Recepten Manager - Programmeer Opdracht

Maak een Python-programma dat een eenvoudige recepten manager bouwt met behulp van tuples en zoekalgoritmes.

## Tuple Structuur

Elke recept wordt voorgesteld als een tuple:

```python
(recept_naam, bereidingstijd, porties, keuken_type, beoordeling)
```

## Voorbeelddata

```python
recepten = [
    ("Spaghetti Carbonara", 20, 4, "Italiaans", 4.5),
    ("Erwtensoep", 45, 6, "Nederlands", 4.2),
    ("Pad Thai", 25, 3, "Thais", 4.6),
    ("Tosti", 5, 1, "Nederlands", 3.8),
    ("Pizza Margherita", 30, 2, "Italiaans", 4.0)
]
```

## Te Schrijven Functies

### 1. Gesorteerde Invoeging

Schrijf een functie `voeg_recept_toe(recepten_lijst, nieuw_recept)` die een nieuw recept toevoegt aan de lijst, gesorteerd op beoordeling (hoogste eerst).

### 2. Lineair Zoeken

Schrijf een functie `zoek_op_keuken(recepten_lijst, keuken_type)` die alle recepten van een bepaald keuken type teruggeeft.

### 3. Binair Zoeken

Schrijf een functie `zoek_op_tijd(recepten_lijst, bereidingstijd)` die een recept zoekt met een exacte bereidingstijd via binair zoeken. Je mag ervan uit gaan dat de lijst al gesorteerd is.

## Testcode

Experimenteer met onderstaande testcode om je functies te controleren:

## Verwachte Output

```
=== Recepten gesorteerd op beoordeling ===
Pad Thai - 4.6 sterren
Spaghetti Carbonara - 4.5 sterren
Erwtensoep - 4.2 sterren
Pizza Margherita - 4.0 sterren
Tosti - 3.8 sterren

=== Nederlandse recepten ===
Erwtensoep (45 min)
Tosti (5 min)

=== Recept met 25 minuten ===
Gevonden: Pad Thai
```

## Tips

- **Gesorteerde invoeging**: Zoek de juiste positie in de lijst en voeg het recept daar toe.
- **Lineair zoeken**: Controleer elk recept één voor één op het keuken type.
- **Binair zoeken**: Sorteer de lijst op bereidingstijd en gebruik binair zoeken voor efficiëntie.

Experimenteer met verschillende recepten en zoekopdrachten om je manager uit te breiden!
