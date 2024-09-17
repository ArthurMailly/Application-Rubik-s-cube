from math import sqrt

#Ce sont les opérations qui servent à fournir les statistiques pour la scène experte

def mean(l): #moyenne
    moy = 0
    n = len(l)
    for i in range(n):
        moy += l[i]
    moy /= n
    return moy


def std(l): #écart-type
    n = len(l)
    m = mean(l)
    s = 0
    for i in range(n):
        s += abs(l[i] - m) ** 2
    s /= n
    s = sqrt(s)
    return s


def pbest(l): #meilleur temps
    pb = l[0]
    for i in range(len(l)):
        if l[i] < pb:
            pb = l[i]
    return pb


def pworst(l): #pire temps
    w = l[0]
    for i in range(len(l)):
        if l[i] > w:
            w = l[i]
    return w


def ao(n, l): #average of n
    best = l[len(l) - n]
    worst = l[len(l) - n]
    for i in range(len(l) - n, len(l)):
        if l[i] < best:
            best = l[i]
        if l[i] > worst:
            worst = l[i]
    averageof = 0
    for i in range(len(l) - n, len(l)):
        if l[i] != best and l[i] != worst:
            averageof += l[i]
    averageof /= n - 2
    return averageof
