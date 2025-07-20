def tuple_pyramide(n, s):
    resultaat = s
    for niveau in range(2, n + 1):
        nieuw_resultaat = []
        for _ in range(niveau):
            nieuw_resultaat.append(resultaat)
        resultaat = tuple(nieuw_resultaat)
    print(resultaat)