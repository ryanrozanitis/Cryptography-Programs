# I am using Python 3.7 for all the programs in this zip file.
# I also used Python 3.7 for the programs on the Midterm but maybe that doesn't matter anymore

from MulitplicativeModularInverseOperation import MultiplicativeModularInverseOperation


def FindAndOrderAllPointsOnEC(A, B, pr):
    # brute force... will take a bit for larger primes.
    X = []
    Y = []
    for n in range(0, pr):
        X.append(n)
        Y.append(n)

    # y^2 = x^3 + 2x + 2 (mod 17)
    intersect = []
    for X1 in X:
        tmp = ((X1**3 + A*X1 + B) % pr)
        for Y1 in Y:
            if (Y1**2) % pr == tmp:
                intersect.append([X1, Y1])
    print("order:", len(intersect) + 1)
    print("points:", intersect)
    return len(intersect) + 1, intersect


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


# y^2 = x^3 + 2x + 2 (mod 17)
# prime = 17
# a = 2
# b = 2

# y^2 = x^3 + 7x + 15 (mod 3571)
prime = 8011
a = 20
b = 9
how_many_generators_do_you_want = 0 # 0 will find all, otherwise find up to the number requested
ord, pts = FindAndOrderAllPointsOnEC(a, b, prime)
breakout = False
# FindAndOrderAllPoints(P, prime)

generators = []

for pt in pts:
    P = pt
    # print("P: ", P)

    Q = PointDoubling(P, a, b, prime)
    tmp = Q
    # print("2 P: ", Q)

    for i in range(3, ord):
        if P in generators:
            # we have symmetry, so when we find a generator, we also save the last value and add it to the list.
            # then here we check if it is in the list so we don't have to compute
            # cuts down half of the computations.
            break

        Q = PointAddition(P, Q, prime)
        # print(i, "P: ", Q)

        if P[0] == Q[0]:
            # print("order of group: ", i + 1)
            break

    if i == ord or i == ord - 1 or i == ord + 1:
        # we found a generator

        if abs(how_many_generators_do_you_want) != 0:
            generators.append(P)
            if len(generators) >= abs(how_many_generators_do_you_want):
                break # remove this guy to get more generators
            generators.append(Q)
            if len(generators) >= abs(how_many_generators_do_you_want):
                break # remove this guy to get more generators
        else:
            generators.append(P)
            generators.append(Q)
        # break

for gen in generators:
    print(gen, "is a generator")

