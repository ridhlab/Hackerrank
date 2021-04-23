def checkM1(s, d, m):
    result = 0
    for i in s:
        if d == i:
            result += 1
        else:
            pass
    return result

def checkM23(s, d, m, bol):
    result = 0
    if m == 2:
        for i in range(len(s) - 1):
            if s[i] + s[i+1] == d and bol:
                result += 1
            else:
                pass
            if bol == False:
                a = s[i] + s[i+1]
                return a
        if bol == True:
            return result
        else:
            pass
    else:
        for i in range(m-1, len(s)):
            a = checkM23(s[i-(m-1):i], d, m-1, False)
            if bol == True:
                if  a + s[i] == d:
                    result += 1
                else:
                    pass
            elif bol == False:
                b = a + s[i]
                return b
        return result
    
def checkM4(s, d, m, bol):
    lenS = len(s)
    result = 0
    if m == 4:
        for i in range(m-1, lenS):
            a = checkM23(s[i-(m-1):i], d, m-1, False)
            if a + s[i] == d and bol:
                result += 1
            else:
                pass
            if bol == False:
                b = a + s[i]
                return b
        if bol == True:
            return result
    else: 
        for i in range(m-1, lenS):
            a = checkM4(s[i-(m-1):i], d, m-1, False)
            if bol == True:
                if a + s[i] == d:
                    result += 1
                else:
                    pass
            elif bol == False:
                b = a + s[i]
                return b 
        return result
        
def checkSame(s, d, m):
    sumS = sum(s)
    if sumS == d:
        return 1
    
            
def birthday(s, d, m):
    if m == 1:
        result = checkM1(s, d, m)
        return result
    if m == len(s):
        result = checkSame(s, d, m)
        return result
    elif m > 1 and m < 4:
        result = checkM23(s, d, m, True)
        return result
    elif len(s) > 3 and m > 3:
        result = checkM4(s, d, m, True)
        return result
    
if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
    print(result)

