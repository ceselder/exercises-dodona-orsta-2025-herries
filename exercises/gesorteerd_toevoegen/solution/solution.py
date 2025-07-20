def voeg_toe_gesorteerd(lijst, getal):
    length = len(lijst)
    for i in range(0, length):
        if lijst[i] > getal:
            return lijst[0:i] + [getal] + lijst[i:length]
    return lijst + [getal]