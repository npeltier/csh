from random import randrange

NB_TIRAGE = 20000
WIDTH = 100

def tirage():
    return [randrange(6) + 1 for de in range(4)]

def sommes(des):
    _sommes = []
    for de in range(4):
        for autre in range(4):
            if (de != autre):
                _sommes.append(des[de] + des[autre])
    return set(_sommes)

def stats(dejaTire):
    stats = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10:0, 11:0, 12:0}
    for jeter in range(NB_TIRAGE):
        des = tirage()
        _sommes = sommes(des)
        if (not _sommes.intersection(dejaTire)):
            for resultat in _sommes:
                stats[resultat] += 1
    return stats

def runAndPlot(dejaTire, overallMax):
    print('### Probabilité de tirage ayant pris les lignes', dejaTire, '\n')
    data = stats(dejaTire)
    ratio = overallMax / max(data.values())
    for ligne in range(2,13):
        gauge = "□" * int(data[ligne] * ratio * WIDTH / NB_TIRAGE)
        espacement = " " * (1 - int(ligne / 10))
        print (ligne, espacement, gauge, "\n")

print('# Aide Can\'t stop\n')
canonical = stats({})
overallMax = canonical[7]
for ligne1 in range(2,13):
    for ligne2 in range (ligne1, 13):
        if (ligne1 != ligne2):
            runAndPlot({ligne1, ligne2}, overallMax)