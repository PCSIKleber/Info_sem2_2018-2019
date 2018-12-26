exemple = '''tc.drf.t
ppp.pppp
...p...c
.....f..
..C..P..
..P.D.P.
PP.....P
T.F.RFCT'''

def fabrique_echiquier(s):
    L = []
    for line in s.split('\n'):
        L.append(list(line))
    return L

exemple_echiquier = fabrique_echiquier(exemple)

def affiche_echiquier(echiquier,raw=False):
    s = ''
    if raw:
        for line in echiquier:
            s += ''.join(line) + '\n'
        return s
    else:
        for line in echiquier:
            s += ' ' + str(line) + ',\n'
        return '[' + s[1:-2] + ']'
