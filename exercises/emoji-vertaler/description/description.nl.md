# Opgave: Emoji Vertaler met Tuples 😄➡️📱

In deze opdracht ga je een eenvoudige **emoji-vertaler** maken met behulp van **tuples** in Python. Je gebruikt een lijst van tuples waarin elk tuple een woord en een bijbehorende emoji bevat.

---

Je krijgt als argument een lijst van tuples van woorden en emojis

```python
emoji_lijst = [
    ("blij", "😊"),
    ("verdrietig", "😢"),
    ("boos", "😠"),
    ("cool", "😎"),
    ("verliefd", "😍")
]
```

Elke tuple in de lijst bevat:

- een **woord** (zoals `"blij"`)
- een **emoji** (zoals `"😊"`)

Je krijgt een **zin** als input. Je moet elk woord in de zin dat voorkomt in de emoji-lijst vervangen door de bijbehorende emoji.

Schrijf een functie `vertaal_emoji(zin, emoji_lijst)` die een zin en een emoji-lijst als argumenten neemt en de vertaalde zin retourneert.

### Voorbeeld

```python
zin = "ik ben blij maar soms verdrietig"
```

Na vertaling:

```
"ik ben 😊 maar soms 😢"
```
