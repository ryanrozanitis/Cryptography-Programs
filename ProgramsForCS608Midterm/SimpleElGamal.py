from math import sqrt


def prime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True


def Euclid_GCD(val1, val2):
    if (val1 < val2):
        (val1, val2) = (val2, val1)
        # Swap them so we can do arithmetic properly if needed

    remainder = val1 % val2
    while (remainder != 0):
        tmp1 = val1
        tmp2 = val2
        val1 = tmp2
        val2 = tmp1 % tmp2
        remainder = val1 % val2

    return val2


def find_small_generators(num, howmany):
    # print("1 ")
    i = 3
    j = 0

    while i < num:
        if (Euclid_GCD(i, num)) == 1:
            # if GCD is 1, then this is a generator.
            # print(i, " ")
            return i
            j = j + 1

        i = i + 1
        if howmany == j:
            i = num


def squareandmultiply(b, ex, modulus):
    # binary representation of the exponent
    exp = bin(ex)

    # Replace the 0b from the bin function.
    eval = b % modulus

    # skip first 3...
    # 0b takes up 2 characters, so we can ignore.
    # don't square on 1st digit ever. x^0 = 1
    for i in range(3, len(exp)):
        # The square for every iteration
        eval = (eval * eval) % modulus
        if (exp[i:i + 1] == '1'):
            # Can just apply modulus to everything. Modular arithmetic is like that.
            # The multiply only when bit is 1
            eval = ((eval % modulus) * (b % modulus)) % modulus

    return (eval % modulus)


def MultiplicativeModularInverseOperation(number_to_be_inverted, modulus):
    # Check to make sure we have the modulus > number_to_be_inverted
    if number_to_be_inverted > modulus:
        number_to_be_inverted = number_to_be_inverted % modulus

    # check if GCD(inverse, modulus) is 1
    gcd = Euclid_GCD(number_to_be_inverted, modulus)

    if gcd == 1:
        # number to be inserted and modulus are coprime, totient = modulus -1
        # and, inverse = number^(modulus-2) mod modulus
        # The third argument of the pow function ends up turning this into modular exponentiation, pretty nice.
        # this pow() function is a way to double check if my code is correct.
        # inverse = pow(number_to_be_inverted, modulus-2, modulus)
        #
        # Ok, so I finally figured it out. if the number is not prime, I need to apply the squareandmultiply
        # algorithm and look for the next time that it returns a 1. Once I find that, I know that the next inverse
        # is the real inverse I am looking for, and can use that as my inverse. At least with the sample problems,
        # this method worked for all of them. Potentially not a scalable solution, as it is bad for large numbers.
        verify = prime(modulus)
        if verify:
            inverse = squareandmultiply(number_to_be_inverted, modulus - 2, modulus)
        else:
            u = 1
            while u < modulus:
                inverse = squareandmultiply(number_to_be_inverted, modulus - u, modulus)
                if inverse == 1:
                    inverse = squareandmultiply(number_to_be_inverted, modulus - (u + 1), modulus)
                    return inverse
                u = u + 1

        # print("Multiplicative Modular Inverse:", inverse)
        return inverse
    else:
        print("There is no multiplicative inverse")
        return 0


def encrypt_with_elgamal(gen, mod, B, secretK, message):
    Pb = squareandmultiply(gen, B, p)
    print("Pb: g^b mod p =", Pb)

    o = 0
    while Pb == 1:
        # bad, look for another Pb
        o = o + 1
        Pb = squareandmultiply(gen, B - o, mod)
        print("Pb: g^b mod p =", Pb)

    if Pb != 1:
        M = squareandmultiply(Pb, secretK, mod)
        print("M: Pb^k mod p =", M)

        o = 0
        while M == 1:
            # bad, look for another M
            o = o + 1
            M = squareandmultiply(gen, secretK - o, mod)
            print("M: Pb^k mod p =", M)

        if M != 1:
            cipher = (message * M) % p
            print("C: m*M mod p =", cipher)

            hint = squareandmultiply(gen, secretK, mod)
            print("H: g^k mod p =", hint)

    return cipher, hint


def decrypt_with_elgamal(d_cipher, d_hint, d_p, d_b):
    d_r = squareandmultiply(d_hint, (d_p - 1 - d_b), d_p)
    print("R: H^(p-1-b) mod p =", d_r)

    d_d = (d_cipher * d_r) % d_p
    # print("D:", d_d)

    return d_d


p = 1299841
g = int(find_small_generators(p, 1))
print("g:", g)
b = 23
a = 29
k = 57
msg = 10346
sign_M = 11
print("m:", msg)

no_signature = 0
if no_signature != 1:
    r = 7 # just choose any number that is gcd(r, p-1) = 1 and 0 < r < p-1
    sign_k = squareandmultiply(g, r, p)
    print(sign_k)
    R = 11 # again, gcd(R, p-1) != 1
    X = squareandmultiply(g, R, p)
    print("X:",X)
    inverse_R = MultiplicativeModularInverseOperation(R, p - 1)
    print("R^-1:", inverse_R)
    Y = ((sign_M - (r * X)) * inverse_R) % (p - 1)
    print("Y:", Y)

    # remove signature...
    receiver_computes = (pow(sign_k, X) * pow(X, Y)) % p
    receiver_verifies = squareandmultiply(g, sign_M, p)
    if receiver_verifies == receiver_computes:
        print("Message is Authenticated.", receiver_computes, "=", receiver_verifies)
    else:
        print("Message is Not Authentic.", receiver_computes, "=", receiver_verifies)

# idk why we are given A, we don't use it...
# Weird.
C, H = encrypt_with_elgamal(g, p, b, k, msg)

D = decrypt_with_elgamal(C, H, p, b)
print("D: C*R mod p =", D)

# print(str(g) + "^" + str(b), "mod", p, "=", squareandmultiply(g, b, p))
