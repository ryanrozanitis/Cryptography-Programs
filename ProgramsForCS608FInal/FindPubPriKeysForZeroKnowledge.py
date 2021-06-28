# x^2 * P mod N = 1
p = 59
q = 61
N = p*q

PubA = []
PriA = []

P = 2
s = 2
while len(PubA) < 10:
    tmp = ((s * s) * P) % N
    #print(tmp)

    if tmp == 1:
        print("P:", P, "S:", s)
        PubA.append(P)
        PriA.append(s)
        P = P + 1
        s = 2
    elif s >= N:
        P = P + 1
        s = 2
    else:
        s = s + 1

# print(PubA)
# print(PriA)
