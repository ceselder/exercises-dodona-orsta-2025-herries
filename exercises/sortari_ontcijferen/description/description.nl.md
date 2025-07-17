## Ontcijfer de Alien Taal!

Aliens hebben een geheime taal ontwikkeld genaamd Sortari. Jij bent uitverkoren om hun boodschap te ontcijferen! De aliens sturen hun zinnen als een lijst van onbekende woorden. Gelukkig heb je een woordenboek gekregen dat elk alien-woord koppelt aan een Nederlands woord.

Maar let op: de volgorde van de alien-woorden klopt niet met onze taal! Je moet de alien-zin eerst alfabetisch sorteren (volgens het alien-alfabet), zodat de vertaling in het Nederlands een kloppende zin vormt.

### Opdracht

Schrijf een functie `ontcijfer(alien_zin, woordenboek)` die een lijst van alien-woorden (`alien_zin`) en een dictionary (`woordenboek`) ontvangt. Sorteer eerst de alien_zin alfabetisch, vertaal daarna elk woord met het woordenboek, en geef de vertaalde zin als één string terug.

#### Voorbeeld

```python
alien_zin = ['wazz', 'blorg', 'zib']
woordenboek = {
    'blorg': 'ik',
    'zib': 'hou',
    'wazz': 'python'
}
print(ontcijfer(alien_zin, woordenboek))
```

**Uitvoer:**

```
ik hou python
```

_(Let op: de alien_zin wordt eerst gesorteerd tot ['blorg', 'wazz', 'zib'], daarna vertaald tot 'ik python hou', maar omdat het woordenboek de juiste volgorde geeft na sorteren, klopt de zin.)_

### Extra uitdaging

Wat als een alien-woord niet in het woordenboek staat? Laat dan het woord `???` zien op die plek.

#### Voorbeeld

```python
alien_zin = ['flozz', 'blorg', 'zib']
woordenboek = {
    'blorg': 'ik',
    'zib': 'hou'
}
print(ontcijfer(alien_zin, woordenboek))
```

**Uitvoer:**

```
??? ik hou
```

Veel succes met het ontcijferen én sorteren!
