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


# this is for RSA encrypt
m = 31963816
print("Original Message:", m)
p = 1299869
q = 1299877
n = p*q
print("n (p*q):", n)
phi_n = (p-1)*(q-1)
print("phi(n):", phi_n)

# ok, now for signing
r = 104827
s = 104831
w = r*s  #n was already used ...
# print("w (for signing, r*s):", w)
phi_w = (r-1)*(s-1)
# print("phi(w) (for signing):", phi_w)

# I don't know what will be on the test, so here is my take on if I get e or not
are_we_given_e = 0
if are_we_given_e == 0:
    v = 1
    while v < phi_n:
        v = v + 1

        this_gcd = Euclid_GCD(phi_n, v)
        if this_gcd == 1:
            e = v
            print("encryption key:", e)
            v = phi_n
else:
    # NOTE TO ME... don't forget to set doRSA and are_we_given_e
    # if we are given e on the midterm than just go here
    e = 53
    gcd = Euclid_GCD(e, phi_n)
    print(gcd)
    print("encryption key:", e)

# Same as above but with g
# This really could just be a function but...
# I don't have time
are_we_given_g = 0
if are_we_given_g == 0:
    v = 1
    while v < phi_w:
        v = v + 1

        this_gcd = Euclid_GCD(phi_w, v)
        if this_gcd == 1:
            g = v
            print("signature:", g)
            v = phi_w
else:
    # copy paste from above, but for signing
    # its good I predicted this while coding this, so now I can just implement signing real quick.
    g = 53
    gcd = Euclid_GCD(g, phi_w)
    print(gcd)
    print("signature:", g)

# yep, bad for large numbers.
# I don't know how else to solve it
# I guess bad is relative, takes like 20 seconds to solve both h and e in the example problem from canvas
# h = MultiplicativeModularInverseOperation(g, phi_w)
# print("to unsign (g^-1 mod phi(w):", h)

# at this point I have e, need to get d
# de mod phi_n = 1
# de = 1 mod phi_n
# d = 1* (e^-1) mod phi_n ???
d = MultiplicativeModularInverseOperation(e, phi_n)
print("decryption key:", d)

# Sign, then encrypt
# Can comment out next two lines if we don't need is signing.
#x = squareandmultiply(m, g, w)
#print("signed message:", x)

# encrypt with RSA
c = squareandmultiply(m, e, n)
print("ciphertext:", c)

# decrypt
decrypted_m = squareandmultiply(c, d, n)
print("Decrypted Message:", decrypted_m)

# remove signature
#contents = squareandmultiply(decrypted_m, h, w)
#print("Original Message after being signed, encrypted, decrypted, and signature removed:", contents)
