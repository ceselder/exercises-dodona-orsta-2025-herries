def merge_lijsten(lijst1, lijst2):
    i = 0 
    j = 0 
    resultaat = []
    while i < len(lijst1) and j < len(lijst2):
        if lijst1[i] < lijst2[j]:
            resultaat.append(lijst1[i])
            i += 1
        else:
            resultaat.append(lijst2[j])
            j += 1

    while i < len(lijst1):
        resultaat.append(lijst1[i])
        i += 1

    while j < len(lijst2):
        resultaat.append(lijst2[j])
        j += 1
    return resultaat

