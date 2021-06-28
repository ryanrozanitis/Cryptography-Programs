def convertToBase26(p, blk, b):
    # First need to break into blocks.
    out = [(p[i:i + blk]) for i in range(0, len(p), blk)]
    # print out the blocks just to see we have it correct
    print(out)
    print()
    tmp = []

    # num is going to be the numerical representation
    # r is the block length, so we start at r-1 for exponents
    # convert char C to a number. use ASCII. 97 = a, 98 = b, so ord(a)-97=0
    # z is the first part formula in steps... SUM (AsubR * L^(r-1)) = num(m)
    # num = num + z... the summation
    # then decrement r so we can do the next letter in the block.
    # print out when done with a block, show both the block text and the compressed numeric representation in base 26
    for block in out:
        conversion = []
        formula = []
        num = 0
        r = len(block) - 1
        # computing r like this allows us to handle blocks at the end that are smaller than the block size.
        for c in block:
            x = convertLetterToNumber(c)
            z = x*(b**r)
            num = num + z
            conversion.append(str(x).zfill(2))
            # print(c, str(x).zfill(2))
            formula.append(str(x).zfill(2) + "*" + str(b) + "^" + str(r))
            r = r - 1

        # print(block + "=" + str(conversion))
        print(block + "=" + str(formula) + "=" + str(num))
        # print(block + "=" + str(num))
        # print()
        tmp.append(block + ":" + str(num))

    return tmp


# I know PyCharm wants me to use all lowercase for function names, but it is so much more readable like this.
# IMO better...
def convertLetterToNumber(input):
    lowercase = input.lower()
    for character in lowercase:
        number = ord(character) - 97
        return number


base = 26
blockSize = 6
# plaintext = "Do not send files as attachments to emails"
# plaintext = "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# plaintext = "azzz"
# plaintext = "agcrypto"
# plaintext = "NJIT"
plaintext = "crypto"
plaintext = plaintext.replace(" ", "")
plaintext = plaintext.replace("'", "")
plaintext = plaintext.replace(".", "")
plaintext = plaintext.replace(",", "")
plaintext = plaintext.replace("1", "")
plaintext = plaintext.replace("2", "")
plaintext = plaintext.replace("3", "")
plaintext = plaintext.replace("4", "")
plaintext = plaintext.replace("5", "")
plaintext = plaintext.replace("6", "")
plaintext = plaintext.replace("7", "")
plaintext = plaintext.replace("8", "")
plaintext = plaintext.replace("9", "")
plaintext = plaintext.replace("0", "")
plaintext = plaintext.lower()


# Good way to check, blocks that start with 'a' should be low numbers, blocks start with z should be high.
# with blockSize = 4, a = 00 so 00*26^3 = 0, b = 1 so 01*26^3 = 17576, z = 25 so 25*26^3 = 439400
# The first character in the block holds way more influence on the value of the numeric representation.
# so a block with azzz should be 17575.
numericRepresentation = convertToBase26(plaintext, blockSize, base)
print()
for compressednum in numericRepresentation:
    print(compressednum)
