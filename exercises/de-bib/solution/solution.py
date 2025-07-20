def voeg_gesorteerd_toe(gesorteerde_lijst, nieuw_boek):
    for i in range(len(gesorteerde_lijst)):
        if nieuw_boek.lower() < gesorteerde_lijst[i].lower(): 
            gesorteerde_lijst.insert(i, nieuw_boek)
            return gesorteerde_lijst
    gesorteerde_lijst.append(nieuw_boek)
    return gesorteerde_lijst