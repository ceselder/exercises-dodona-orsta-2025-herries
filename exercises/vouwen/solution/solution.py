def bepaal_winnaar(bord):
    lijnen_om_te_checken = []

    for i in range(3):
        lijnen_om_te_checken.append((bord[i][0], bord[i][1], bord[i][2])) # Rijen toevoegen
        lijnen_om_te_checken.append((bord[0][i], bord[1][i], bord[2][i])) # Kolommen toevoegen

    # Voeg diagonalen toe
    lijnen_om_te_checken.append((bord[0][0], bord[1][1], bord[2][2]))
    lijnen_om_te_checken.append((bord[0][2], bord[1][1], bord[2][0]))

    for lijn in lijnen_om_te_checken:
        if lijn == ("X", "X", "X"):
            return "X wint"
        elif lijn == ("O", "O", "O"):
            return "O wint"

    return "niemand wint"