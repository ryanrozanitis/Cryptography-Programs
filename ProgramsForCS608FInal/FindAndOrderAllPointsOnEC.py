# I am using Python 3.7 for all the programs in this zip file.
# I also used Python 3.7 for the programs on the Midterm but maybe that doesn't matter anymore


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


# y^2 = x^3 + 2x + 2 (mod 17)
prime = 17
a = 2
b = 2

# y^2 = x^3 + 7x + 15 (mod 3571)
prime = 3571
a = 7
b = 15
FindAndOrderAllPointsOnEC(a, b, prime)
# FindAndOrderAllPoints(P, prime)
