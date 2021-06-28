# I am using Python 3.7 for all the programs in this zip file.
# I also used Python 3.7 for the programs on the Midterm but maybe that doesn't matter anymore
from MulitplicativeModularInverseOperation import MultiplicativeModularInverseOperation


def PointDoubling(P, A, B, pr):
    XP = P[0]
    YP = P[1]
    # inv_YP = MultiplicativeModularInverseOperation(2 * YP, pr)
    inv_YP = pow(2 * YP, pr - 2, pr)
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


# P = [0, 3]
# Q = P
# a = 2
# b = 9
# prime = 23

# P = [5, 1]
# Q = P
# a = 2
# b = 2
# prime = 17

# P = [16, 3096]
# Q = P
# a = 7
# b = 15
# prime = 3571
# scalar_multiply_count = 150

# print(PointAddition([5, 12], [5, 11], 23))

# P = [12, 17]
# Q = P
# a = 2
# b = 9
# prime = 23
# scalar_multiply_count = 6

P = [18, 14]
Q = P
a = 2
b = 9
prime = 23
scalar_multiply_count = 23


tmp_Q = PointDoubling(P, a, b, prime)
# print("2P", Q)
if P[0] != tmp_Q[0]:
    for i in range(3, 2**32):
        tmp_Q = PointAddition(P, tmp_Q, prime)
        # print(i, "P", Q)

        if P[0] == tmp_Q[0]:
            print("order of group: ", i + 1)
            print("scalar multiple count: ", scalar_multiply_count)
            order = i + 1
            break
else:
    order = 2

scalar_multiply_count = scalar_multiply_count % order
iterations = 1
print(str(iterations) + "P", Q)
if order == 2:
    print("2P", PointDoubling(P, a, b, prime))
while iterations < scalar_multiply_count:
    iterations = iterations + 1
    if P == Q:
        # print("doubling")
        Q = PointDoubling(P, a, b, prime)
        if iterations == scalar_multiply_count:
            print(str(iterations) + "P", Q)
    else:
        # print("addition")
        # if Q[0] - P[0] != 0:
        Q = PointAddition(P, Q, prime)
        if iterations == scalar_multiply_count:
            print(str(iterations) + "P", Q)
        # else:
        #     print(str(iterations) + "P point at infinity")
        #     break

