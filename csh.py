from random import randrange
import matplotlib.pyplot as plt

NB_TIRAGE = 10000

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

data = stats({7,9})
plt.bar(data.keys(), data.values())
plt.show()