def binaire_zoek_invoegpositie(gesorteerde_lijst, nieuw_boek):
    links = 0
    rechts = len(gesorteerde_lijst)
    #links en rechts samen definiëren het zoekgebied

    stappen = 0

    while links < rechts:
        stappen += 1
        midden = (links + rechts) // 2
        if nieuw_boek < gesorteerde_lijst[midden]:
            rechts = midden
        else:
            links = midden + 1

    return links, stappen