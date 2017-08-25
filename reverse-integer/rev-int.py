# reverse digits of an integer
# python2

#get range of signed 32bit twos compliment
MAX = (0x1 << 31) - 1
#print(format( MAX, '02x'))

MIN = ~((0x1 << 31) -1)
#print(format( MIN, '02x'))

def rev_int(x):
    temp = x

    #check if input is negative
    check = False
    if x < 0:
        temp = x * -1
        check = True

    #reverse string
    buff = str(temp)[::-1]
    revd = int(buff)

    if check:
        #originally negative item
        if revd < MIN:
            return 0
        return -(revd)
    #orig. positive item
    if revd > MAX:
        return 0
    return revd

        
