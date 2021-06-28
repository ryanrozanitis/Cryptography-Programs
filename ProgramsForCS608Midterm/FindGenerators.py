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
            print(i, " ")
            j = j + 1

        i = i + 1
        if howmany == j:
            i = num


def find_largest_generators(num, howmany):
    i = num
    j = 0

    # Basically just the reverse of find_generators. Start from the top and go down.
    while i > 2:
        if (Euclid_GCD(i, num)) == 1:
            print(i)
            j = j + 1

        i = i - 1
        if howmany == j:
            i = 1


a = 1299841
amount = 3
# a = 200000
find_small_generators(a, amount)
# find_largest_generators(a, amount)
