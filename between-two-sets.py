#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def KPK(a1, a2, batas):
    listMultiples = []
    for i in range(a1, batas, a1):
        listMultiples.append(i)
    for i in listMultiples:
        if i % a2 == 0:
            KPK = i
            break
        else:
            pass
    return KPK

def preparation(a, lenA, batas, b):
    bc = KPK(a[0], a[1], batas)
    if lenA > 2:
        for i in range(2, lenA):
            bc = KPK(bc, a[i], batas)
    else:
        pass
    listMultiplesKPK = []
    for i in range(bc, batas, bc):
        listMultiplesKPK.append(i)
    return listMultiplesKPK

def checkElement(bil, listCheck):
    listBol = []
    for i in listCheck:
        if bil == i:
            listBol.append(True)
            break
        else:
            if i == listCheck[-1]:
                listBol.append(False)
            else:
                pass
    return listBol

def check(resultListNdim):
    x = resultListNdim[0]
    for t in resultListNdim[1:]:
        for i in x:
            a = checkElement(i, t)
            if a[0] == False:
                x.remove(i)
            else:
                pass
    return x

def faktor(bil):
    listFaktor = []
    for i in range(1, bil+1):
        if bil % i == 0:
            listFaktor.append(i)
    return listFaktor

def getTotalX(a, b):
    a.sort()
    b.sort()
    lenA = len(a)
    lenB = len(b)
    temp = True
    if lenA == 1 and a[0] != 1:
        for i in b:
            if i % a[0] == 0:
                pass
            else:
                temp = False
                break
        if temp == True:
            return 1
        else:
            return 0
    elif lenA == 1:
        if a[0] == 1:
            if lenB == 1:
                return len(faktor(b[0]))
            else:
                listFaktorNdim = []
                for i in b:
                    cd = faktor(i)
                    listFaktorNdim.append(cd)
                bd = check(listFaktorNdim)
                return len(bd)
    test = True
    if a[0] > b[-1]:
        return 0
        test = False
    if test == True and lenA > 1:
        batasA = b[0] + 1
        batasB = b[-1] + 1
        KPKA = preparation(a, lenA, batasA, b)
        resultListNdim = []
        for i in b:
            resultList = []
            for bc in KPKA:
                if i % bc == 0:
                    resultList.append(bc)
                else:
                    pass
            resultListNdim.append(resultList)
        result = check(resultListNdim)
        lenResult = len(result)
        return lenResult
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
