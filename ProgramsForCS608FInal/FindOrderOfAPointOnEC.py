from MulitplicativeModularInverseOperation import MultiplicativeModularInverseOperation


def PointDoubling(P, A, B, pr):
    XP = P[0]
    YP = P[1]
    inv_YP = MultiplicativeModularInverseOperation(2 * YP, pr)
    alpha = ((3 * (XP * XP) + A) * inv_YP) % pr
    # alpha = (3x^2 + a) / (2*y) , where x = xP and y = yP
    XR = ((alpha * alpha) - (2 * XP)) % pr
    YR = (alpha * (XP - XR) - YP) % pr
    return [XR, YR]


def PointAddition(P, Q, pr):
    XP1 = P[0]
    YP1 = P[1]
    XQ1 = Q[0]
    YQ1 = Q[1]
    inv_of_denominator = pow(XQ1 - XP1, pr - 2, pr)
    # print(XQ1, XP1, XQ1 - XP1, inv_of_denominator)
    alpha = ((YQ1 - YP1) * inv_of_denominator) % pr
    # print(alpha)
    XR1 = ((alpha * alpha) - XP1 - XQ1) % pr
    # print(XR1)
    YR1 = (alpha * (XP1 - XR1) - YP1) % pr
    return [XR1, YR1]


P = [9, 922]
a = 20
b = 9
prime = 8001

print("P: ", P)

Q = PointDoubling(P, a, b, prime)
tmp = Q
print("2 P: ", Q)

for i in range(3, 2**32):
    Q = PointAddition(P, Q, prime)
    print(i, "P: ", Q)

    if P[0] == Q[0]:
        print("order of group: ", i + 1)
        break
