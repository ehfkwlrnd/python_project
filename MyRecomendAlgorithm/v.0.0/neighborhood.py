def percent(A, B):
    A_set = set(A.keys())
    B_set = set(B.keys())
    inter = A_set.intersection(B_set)
    union = A_set.union(B_set)

    E = 0
    S = 0
    for e in inter:
        E += 5
        S += abs(A[e] - B[e])
    if E == 0:
        return 0
    return (((len(inter)+len(union))/(len(union)+len(union))) * (1 - S/E))

def recomend(index, users):
    A = users[index]
    users = users[0:index]+users[index+1:]
    Q = []
    S = set()
    for user in users:
        p = percent(A, user)
        if p > 0.5:
            Q.append((p, user))
            S = S.union(set(user.keys()))
    S = S.difference(set(A.keys()))
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
        if D/M >= 3:
            rL.append({'element' : e, 'probability' : M/R, 'evaluation' : D/M})
    return rL
        
    


A = {'a':5, 'b':1}
B = {'a':5, 'c':3, 'd':4}
C = {'a':5, 'b':2, 'c':2}#, 'd':0, 'e':3
D = {'a':2, 'b':5}
E = {'a':1}
F = {'a':5, 'b':1,'e':5}

users = [A, B, C, D, E, F]

##print(recomend(2, users))
print(percent(A, E))
##AB = percent(A, B)
##AC = percent(A, C)
##AD = percent(A, D)
##BD = percent(B, D)
##DE = percent(D, E)
##
##print(f'AB : {AB}')
##print(f'AC : {AC}')
##print(f'AD : {AD}')
##
##print(f'BD : {BD}')
##print(f'DE : {DE}')
##
##recomend = (B['c']*AB + C['c']*AC)/(AB+AC)
##print(recomend)
