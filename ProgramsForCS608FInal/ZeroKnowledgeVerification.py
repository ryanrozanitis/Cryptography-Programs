# I can actually always leave a, b, and c as 2, 3, and 4. "Random" selection. Makes it easier for the final.
a = 2
b = 3
c = 4
print("1. Alice randomly selects {a, b, c}: {" + str(a) + ",", str(b) + ",", str(c) + "}")

# predetermined primes by the question
p = 43
q = 47
N = p*q

# Use FindPubPriKeysForZeroKnowledge to find a set of s and p. can choose the lower looking numbers that are output.
# Will make life a bit easier.
s1 = 80
s2 = 40
p1 = 6
p2 = 24

print("2. TA chooses the following")
print("\ts1:", s1)
print("\ts2:", s2)
print("\tp1:", p1)
print("\tp2:", p2)

# Alice sends {A,B,C} to Bob
A = (a*a) % N
B = (b*b) % N
C = (c*c) % N
print("3. Alice computes and sends to Bob")
print("\tA:", A, "   ... a^2 mod N =", a, "*", a, "mod", N)
print("\tB:", B, "   ... b^2 mod N =", b, "*", b, "mod", N)
print("\tC:", C, "   ... c^2 mod N =", c, "*", c, "mod", N)

# E = [ x1  x2 ]
#     [ y1  y2 ]
#     [ z1  z2 ]
# "Randomly" generated matrix. Can modify these to 0's or 1's.
x1 = 0
x2 = 0
y1 = 0
y2 = 0
z1 = 0
z2 = 1
print("4. Bob randomly generates the matrix...")
print("\tE:", x1, x2)
print("\t  ", y1, y2)
print("\t  ", z1, z2)

# Alice computes
M = (a * pow(s1, x1) * pow(s2, x2)) % N
P = (b * pow(s1, y1) * pow(s2, y2)) % N
Q = (c * pow(s1, z1) * pow(s2, z2)) % N
print("5. Alice computes...")
print("\tM:", M, "   ... a(s1^x1 * s2^x2) mod N =", str(a) + "(" + str(s1) + "^" + str(x1), "*", str(s2) + "^" + str(x2) + ") mod " + str(N))
print("\tP:", P, "   ... b(s1^y1 * s2^y2) mod N =", str(b) + "(" + str(s1) + "^" + str(y1), "*", str(s2) + "^" + str(y2) + ") mod " + str(N))
print("\tQ:", Q, "   ... c(s1^z1 * s2^z2) mod N =", str(c) + "(" + str(s1) + "^" + str(z1), "*", str(s2) + "^" + str(z2) + ") mod " + str(N))

# Bob Verifies
B_M = (pow(M, 2) * pow(p1, x1) * pow(p2, x2)) % N
B_P = (pow(P, 2) * pow(p1, y1) * pow(p2, y2)) % N
B_Q = (pow(Q, 2) * pow(p1, z1) * pow(p2, z2)) % N
print("Bob verifies...")
print("\tBob's A:", B_M, "   ... M^2(p1^x1 * p2^x2) mod N =", str(M) + "^2 (" + str(p1) + "^" + str(x1), "*", str(p2) + "^" + str(x2) + ") mod " + str(N))
print("\tBob's B:", B_P, "   ... P^2(p1^y1 * p2^y2) mod N =", str(P) + "^2 (" + str(p1) + "^" + str(y1), "*", str(p2) + "^" + str(y2) + ") mod " + str(N))
print("\tBob's C:", B_Q, "   ... Q^2(p1^z1 * p2^z2) mod N =", str(Q) + "^2 (" + str(p1) + "^" + str(z1), "*", str(p2) + "^" + str(z2) + ") mod " + str(N))

if A == B_M and B == B_P and C == B_Q:
    print("Verified!")
else:
    print("Impostor!")

print("---------------------")

# Bob attempts to impersonate Alice to Carol
# Sends {A, B, C}
print("1. Bob sends the following to Carol to impersonate Alice...")
print("\t{A, B, C}: {" + str(A) + ",", str(B) + ",", str(C) + "}")

# Carol randomly generates a Matrix
x1 = 1
x2 = 0
y1 = 0
y2 = 0
z1 = 0
z2 = 0
print("2. Carol randomly generates the matrix...")
print("\tF:", x1, x2)
print("\t  ", y1, y2)
print("\t  ", z1, z2)

# Bob imitates Alice, sends {M, P, Q}
print("3. Bob imitates Alice, sends...")
print("\t{M, P, Q}: {" + str(M) + ",", str(P) + ",", str(Q) + "}")

# Carol Verifies
C_M = (pow(M, 2) * pow(p1, x1) * pow(p2, x2)) % N
C_P = (pow(P, 2) * pow(p1, y1) * pow(p2, y2)) % N
C_Q = (pow(Q, 2) * pow(p1, z1) * pow(p2, z2)) % N
print("Bob verifies...")
print("\tCarol's A:", C_M, "   ... M^2(p1^x1 * p2^x2) mod N =", str(M) + "^2 (" + str(p1) + "^" + str(x1), "*", str(p2) + "^" + str(x2) + ") mod " + str(N))
print("\tCarol's B:", C_P, "   ... P^2(p1^y1 * p2^y2) mod N =", str(P) + "^2 (" + str(p1) + "^" + str(y1), "*", str(p2) + "^" + str(y2) + ") mod " + str(N))
print("\tCarol's C:", C_Q, "   ... Q^2(p1^z1 * p2^z2) mod N =", str(Q) + "^2 (" + str(p1) + "^" + str(z1), "*", str(p2) + "^" + str(z2) + ") mod " + str(N))

if A == C_M and B == C_P and C == C_Q:
    print("Verified!")
else:
    print("Impostor!")
