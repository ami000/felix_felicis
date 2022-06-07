def flippingBits(n):
    # Write your code here
    str32bit = bin(n)[2:].zfill(32)
    print('str32bit:',str32bit)
    str32bitlist = list(str32bit)
    for i in range(len(str32bitlist)):
        if str32bitlist[i] == '0':
            str32bitlist[i] = '1'
        else:
            str32bitlist[i] = '0'

    return int("".join(str32bitlist), 2)
if __name__ == '__main__':
    q = [2147483647, 1, 0]

    for num in q:
        print(flippingBits(num))