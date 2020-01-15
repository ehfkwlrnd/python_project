class Neighborhood:
    def __init__(self, myInfo, proximity, maxPoint):
        self._me = myInfo
        self._neighbor = []
        self.proximity = proximity
        self.max = maxPoint

    def getMyInfo(self):
        return self._me

    def getNeighbors(self):
        return self._neighbor

    def _percent(self, A, B):
        A_keys = set(A.keys())
        B_keys = set(B.keys())
        ANB = A_keys.intersection(B_keys)
        AUB = A_keys.union(B_keys)

        E = 0
        S = 0
        for e in ANB:
            E += self.max
            S += abs(A[e] - B[e])
        if E == 0:
            return 0
        return (((len(ANB)+len(AUB))/(len(AUB)+len(AUB))) * (1 - S/E))

    def setNeighbors(self, persons):
        for p in persons:
            if self._percent(self._me, p) > self.proximity:
                self._neighbor.append(p)

    def recomend(self, infimum):
        Q = []
        S = set()
        for n in self._neighbor:
            p = self._percent(self._me, n)
            if p > self.proximity:
                Q.append((p, n))
                S = S.union(set(n.keys()))

        S = S.difference(set(self._me.keys()))
        rL = []
        for e in S:
            M = 0
            D = 0
            R = 0
            for q in Q:
                p = q[0]
                v = q[1].get(e)
                if v != None:
                    M += p
                    D += p*v
                    R += 1
            if D/M >= infimum:
                rL.append({'element' : e, 'probability' : M/R, 'evaluation' : D/M})
        return rL


if __name__ == '__main__':
    A = {'a':5, 'b':1}
    B = {'a':5, 'c':3, 'd':4}
    C = {'a':5, 'b':2, 'c':2}#, 'd':0, 'e':3
    D = {'a':2, 'b':5}
    E = {'a':1}
    F = {'a':5, 'b':1,'e':5}
    users = [B, C, D, E, F]

    n = Neighborhood(A, 0.5, 5)
    n.setNeighbors(users)
    print(n.recomend(3))
