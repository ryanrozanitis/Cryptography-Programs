def Euclid_GCD(val1, val2):
    if (val1 < val2) and val1 != 0:
        (val1, val2) = (val2, val1)
        # Swap them so we can do arithmetic properly if needed

    remainder = val1 % val2
    print(val1, "%", val2, "=", remainder)
    while (remainder != 0):
        # With Euclidean algorithm, once we hit 0, we are done.
        tmp1 = val1
        tmp2 = val2
        val1 = tmp2
        val2 = tmp1 % tmp2
        remainder = val1 % val2
        print(val1, "%", val2, "=", remainder)
        # Ok, I haven't used python in a while so I forgot I can just print like this.
        # I was using str(x) in order to print integers for the last few programs...

    return val2


# x = 1029576
# y = 101928
x = 1299841-1
y = 11
greatestCommonDivisor = Euclid_GCD(x, y)
print("GCD of", x, "and", y, "=", greatestCommonDivisor)
