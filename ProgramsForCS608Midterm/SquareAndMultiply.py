def squareandmultiply(b, ex, modulus):
    # binary representation of the exponent
    exp = bin(ex)

    # Replace the 0b from the bin function.
    print("Binary representation of " + str(ex) + " = " + str(exp).replace("0b", ""))
    eval = b % modulus
    # print(eval)
    # square = eval
    # tmp = 1

    j = 0

    # skip first 3...
    # 0b takes up 2 characters, so we can ignore.
    # don't square on 1st digit ever. x^0 = 1
    for i in range(3, len(exp)):
        # print(exp[i:i+1])
        eval = (eval * eval) % modulus
        # print(square)
        if (exp[i:i + 1] == '1'):
            j += 1
            tmp = ((eval % modulus) * (b % modulus)) % modulus
            # print("# of Multiplications = " + str(j) + ": We have a 1, so we multiply ")
            # + str(eval % modulus) + "*" + str(b % modulus) + " mod " + str(modulus) + " = " + str(tmp))

            # Can just apply modulus to everything. Modular arithmetic is like that.
            eval = ((eval % modulus) * (b % modulus)) % modulus

        # else:
        #     print("# of Multiplications = " + str(j) + ": We have a 0, so we don't multiply.")

        # print(eval)

    # str(len(exp) - 3) because 0b is  1st 2 chars and the first binary digit does not get squared ever. x^0 = 1
    print("There are " + str(len(exp) - 3) + " squares and " + str(j) + " multiplications.")
    return (eval % modulus)


# These were the numbers given to me during the 1st quiz. I am like 99% I got that right so can just use here to check.
# Answer should be 616, 20 squares and 12 multiplications.
# base = 8623
# exponent = 1532662
# mod = 1997
base = 23
mod = 1000000007
exponent = mod - 2

print(str(base) + "^" + str(exponent) + " mod " + str(mod) + " = ?")
print(str(base) + "^" + str(exponent) + " mod " + str(mod) + " = " + str(squareandmultiply(base, exponent, mod)))
