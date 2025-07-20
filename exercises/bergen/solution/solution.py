def naar_meters(berg):
    """Zet de afstand van een berg om naar meters."""
    naam, afstand, eenheid = berg
    if eenheid == "kilometer":
      return afstand * 1000
    elif eenheid == "feet":
      return afstand * 0.3048
    else:  # eenheid is "meter"
      return afstand



def sorteer_bergen(bergen_input):
    gesorteerde_lijst = []

    for berg_om_in_te_voegen in bergen_input:
      hoogte_nieuw = naar_meters(berg_om_in_te_voegen)
      invoeg_positie = 0
      while invoeg_positie < len(gesorteerde_lijst) and naar_meters(gesorteerde_lijst[invoeg_positie]) < hoogte_nieuw:
        invoeg_positie += 1
        
      gesorteerde_lijst.insert(invoeg_positie, berg_om_in_te_voegen)
      # dit kan ook: gesorteerde_lijst[0:invoeg_positie] + [berg_om_in_te_voegen] + gesorteerde_lijst[invoeg_positie:]

    print(gesorteerde_lijst)