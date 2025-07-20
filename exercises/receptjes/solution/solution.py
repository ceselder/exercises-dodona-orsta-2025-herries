def voeg_recept_toe(recepten_lijst, nieuw_recept):
    index = 0
    while index < len(recepten_lijst) and recepten_lijst[index][4] > nieuw_recept[4]:
        index += 1
    recepten_lijst.insert(index, nieuw_recept)
    print(recepten_lijst)

def zoek_op_keuken(recepten_lijst, keuken_type):
    resultaat = []
    for recept in recepten_lijst:
        if recept[3].lower() == keuken_type.lower():
            resultaat.append(recept)
    print(resultaat)

def zoek_op_tijd(recepten_sorted, bereidingstijd):
    low = 0
    high = len(recepten_sorted) - 1

    while low <= high: #binair zoeken
        mid = (low + high) // 2
        if recepten_sorted[mid][1] == bereidingstijd:
            print(recepten_sorted[mid])
            break
        elif recepten_sorted[mid][1] < bereidingstijd:
            low = mid + 1
        else:
            high = mid - 1