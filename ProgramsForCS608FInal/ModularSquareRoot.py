# I am using Python 3.7 for all the programs in this zip file. I also used Python 3.7 for the programs on the Midterm
# but maybe that doesn't matter anymore
# NOTE: The link provided in the lectures is not a valid link anymore because of this I implementing using
# Tonelli-Shanks algorithm to do the harder cases of Modular Square Root Operation.

from math import sqrt
from MulitplicativeModularInverseOperation import MultiplicativeModularInverseOperation, squareandmultiply, Euclid_GCD


def legendre_symbol(la, lp):
    ls = squareandmultiply(la, (lp - 1) // 2, lp)
    # print('lp-1', lp - 1)
    # print('lp', lp)
    # print('ls', ls)
    return -1 if ls == lp - 1 else ls


def ModularSquareRoot(prime, A):
    # If p mod 4 = 3, then a has a square root,
    # then r = a^((p+1)/4) mod p
    # n = a
    # prime = p
    # this function solves for r, one root of sqrroot(a) mod p
    # now r = a^((p+1)/4) mod p
    root = 0
    second_root = 0
    if prime == 2:
        print('Prime = 2, Square Roots do not exist!')
    if prime % 2 == 0:
        print('Your "prime" is not a prime. It is divisible by 2!')
    elif A == 0:
        print('a = 0, Square Roots do not exist!')
    elif Euclid_GCD(A, prime) != 1:
        print('a and p are not coprime!')
    elif squareandmultiply(A, (prime - 1) // 2, prime) == (prime - 1):
        print('Square Roots do not exist!')
    elif prime % 4 == 3:
        exponent = (prime + 1) / 4
        # root = pow(n, exponent)
        root = squareandmultiply(A, int(exponent), prime)
        root = root % prime
        second_root = -1 * root
        second_root = second_root % prime
        print('Potential roots: ', int(root), 'mod', prime, '&', int(second_root), 'mod', prime)

        # verify
        verify_r = (root*root) % prime
        verify_2nd_r = (second_root * second_root) % prime
        print(int(root), '*', int(root), 'mod', prime, '=', verify_r)
        print(int(second_root), '*', int(second_root), 'mod', prime, '=', verify_2nd_r)
        # print(verify_r)
        # print(verify_2nd_r)

        if verify_r == a:
            if verify_2nd_r == a:
                print('Square Roots Exist!')
                # , int(root), 'mod', prime, '&', int(second_root), 'mod', prime)
        else:
            print("Square Roots do not exist")

    elif legendre_symbol(A, prime) != 1:
        # print(n, p)
        print('Legendre Symbol != -1, Square Roots do not exist')

    # NOTE: The link provided in the lectures is not a valid link anymore because of this I implementing using
    # Tonelli-Shanks algorithm to do the harder cases of Modular Square Root Operation.
    else:
        # Tonelli-Shanks part
        s = prime - 1
        cnt = 0
        while s % 2 == 0:
            s //= 2
            cnt += 1

        find_first_n = 2 # where n|p = -1
        while legendre_symbol(find_first_n, prime) != -1:
            find_first_n = find_first_n + 1

        x = squareandmultiply(A, (s + 1) // 2, prime)
        b = squareandmultiply(A, s, prime)
        g = squareandmultiply(find_first_n, s, prime)
        r = cnt

        # print('x', x)
        # print('b', b)
        # print('g', g)
        while True:
            t = b
            m = 0
            for m in range(r):
                if t == 1:
                    break
                t = squareandmultiply(t, 2, prime)
                # print('t', t)

            if m == 0:
                root = x
                second_root = (-1 * x) % prime
                break

            # print('m', m)
            # print('r', r)
            # print(2 ** (r - m - 1))
            gs = squareandmultiply(g, int(2 ** (r - m - 1)), prime)
            g = (gs * gs) % prime
            x = (x * gs) % prime
            b = (b * g) % prime
            r = m

        # print('Square Roots do not exist')

    return root, second_root

# NOTE: The link provided in the lectures is not a valid link anymore because of this I implementing using
# Tonelli-Shanks algorithm to do the harder cases of Modular Square Root Operation.

# The problem...
# p is a prime number
# The goal is to learn how to solve equation x^2 = a mod p or
# How to find sqrroot(a) mod p
# If p mod 4 = 3, then a has a square root,
# then r = a^((p+1)/4) mod p

# p = 7
# a = 2       # roots are (4, 3)
# p = 17
# a = 223     # roots are (6, 11)
# p = 113
# a = 2       # roots are (62, 51)
# p = 7
# a = 5       # roots don't exist
p = 10
a = 3       # roots don't exist
print(ModularSquareRoot(p, a))
# print(r)
# second_r = MultiplicativeModularInverseOperation(r, p)
# print(second_r)
