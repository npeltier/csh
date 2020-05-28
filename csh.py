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
    for jete in range(NB_TIRAGE):
        des = tirage()
        _sommes = sommes(des)
        if (not _sommes.intersection(dejaTire)):
            for resultat in _sommes:
                stats[resultat] += 1
    return stats

def tirageCount(tirages = {}):
    tirageCount = {}     
    for l1 in range(2,13):
        for l2 in range(2,13):
            for l3 in range(2,13):
                if (l1 != l2) and (l1 != l3) and (l2 != l3):
                    tirage = [l1, l2, l3]
                    tirage.sort()
                    tirageStr = ",".join(map(str,tirage))
                    tirageCount[tirageStr] = 0
                    tirages[tirageStr] = tirage
    return tirageCount

def classement(): 
    tirages = {}
    tiragesCount = tirageCount(tirages)
    for jete in range(NB_TIRAGE):
        des = tirage()
        _sommes = sommes(des)
        for somme in _sommes:
            for tirageItem in tirages.items():
                if somme in tirageItem[1]:
                    tiragesCount[tirageItem[0]] += 1
    return {k: v for k, v in sorted(tiragesCount.items(), key=lambda item: item[1])}

def runAndPlot(dejaTire, overallMax):
    print('### Probabilité de tirage ayant pris les lignes', dejaTire, '\n')
    data = stats(dejaTire)
    ratio = overallMax / max(data.values())
    for ligne in range(2,13):
        gauge = "□" * int(data[ligne] * ratio * WIDTH / NB_TIRAGE)
        espacement = " " * (1 - int(ligne / 10))
        print (ligne, espacement, gauge, "\n")

print('# Aide Can\'t stop\n')
print('## Probabilités sachant 2 tirages\n')
print("occurences sur ",NB_TIRAGE," d'une combinaison n'étant pas celles déjà tirées\n")
canonical = stats({})
overallMax = canonical[7]
for ligne1 in range(2,13):
    for ligne2 in range (ligne1, 13):
        if (ligne1 != ligne2):
            runAndPlot({ligne1, ligne2}, overallMax)
print('## Classement des combinaisons\n')
print("occurences sur ",NB_TIRAGE," tirs des combinaisons non perdantes\n")
for i in classement().items():
    print(i[1], " fois ", i[0],"\n")
