class Neighborhood:
    def __init__(self, myInfo, proximity, maxPoint):
        self._me = myInfo
        self._neighbor = [] #(근접도, values) 리스트
        self.proximity = proximity #neighbor로 추가할 최소 근접도
        self.max = maxPoint #value 점수의 최대값
        self._S = set() #neighborKeys - mykeys

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

    def setNeighbors(self, users):
        self._S = set()
        mykeys = set(self._me.keys())
        for u in users:
            p = self._percent(self._me, u)
            if p > self.proximity:
                self._neighbor.append((p, u))
                self._S = self._S.union(set(u.keys()))
        self._S = self._S.difference(set(mykeys))

    def recomend(self, infimum):
        rL = [] #recomend List
        for e in self._S:
            M = 0 #근접도의 합
            D = 0 #근접도*e의 점수의 합
            R = 0 #해당 e를 가진 이웃 수
            for n in self._neighbor:
                p = n[0]
                v = n[1].get(e)
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
