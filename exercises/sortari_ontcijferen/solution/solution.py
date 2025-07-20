def ontcijfer(alien_zin, woordenboek):
    alien_zin.sort()
    vertaalde_woorden = [woordenboek.get(woord, '???') for woord in alien_zin]
    vertaalde_zin = ' '.join(vertaalde_woorden)
    print(vertaalde_zin)
