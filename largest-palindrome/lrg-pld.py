#find the largest palindrome made from the product of two n-digit numbers
#author suggests result could be too large so mod the value with 1337
#uses python2

def largestPalindrome(n):

    def test_palindrome(string):
        rev = string[::-1]
        i = 0
        while i < (len(string) / 2):
            if(string[i] != rev[i]):
                return False
            i += 1
        return True

    buff = []
    for i in range( ( 10**n)-1, 1, -1):
        for j in range( ( 10**n)-1, 1, -1):
            temp = i*j
            if( test_palindrome(str(temp))):
                buff.append(temp)

    large_pal = max(buff)
    return large_pal % 1337 

