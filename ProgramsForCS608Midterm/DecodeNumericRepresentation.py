def decodeNumericRepresentation(blks, bse, bsize):
    tmp2 = []
    plaintext = ''
    for block in blks:
        tmp = ''
        numbers = ''
        x = int(block)
        r = bsize
        while r > 0:
            num = x % bse
            tmp = chr(int(num) + 97) + tmp
            numbers = str(int(num)).zfill(2) + numbers
            # print(str(x) + "%" + str(bse) + "=" + str(num) + "=" + tmp)
            x = (x - num) / bse
            r = r - 1
        tmp2 = [tmp] + tmp2
        print(numbers + "=" + tmp)

    for block in tmp2:
        plaintext = block + plaintext

    print()
    print(plaintext)


base = 26
blockSize = 4
blocks = ['62544', '346229', '56327', '82490', '13338', '40200', '241819', '249080', '5712']

decodeNumericRepresentation(blocks, base, blockSize)
