# import os
# import numpy as np
# # from matplotlib import pyplot as plt
# import pandas
# from pandas import Series
# import random
# import array
# import csv
# import itertools
# import math
# from math import comb


def get_bin(x, n): return format(x, 'b').zfill(n)


def PRODP(startindex, endindex, listp):
    PP = 1
    if (endindex < startindex):
        return PP
    else:
        for i in range(startindex, endindex+1):
            PP = PP*listp[i]
        return PP


def SUMTERM(startindex, endindex, listgk, listp):
    if (endindex < startindex):
        PGK = 0
        return PGK
    else:
        PGK = 0
        for i in range(startindex, endindex+1):
            PT = PRODP(i+1, endindex+1, listp)
            print(PT)
            PTM = listgk[i]*PT
            PGK = PGK+PTM
            print(PGK)
        return PGK
#AA = [1,2,4,2,3,5,10]
#CC = [2,2,2,3,3,3,4]
# BB=SUMTERM(2,4,CC,AA)
# print(AA)
# print(BB)


# *************************************************************************************************
SIZE = int(input("Enter the  Size of adder.\n"))
ES = int(input("Is sub-adder of equal size? Enter 1 for equal size, 2 for unequal size\n"))
ECG = int(input(
    "Is carry generator of equal size? Enter 1 for equal size, 2 for unequal size\n"))

SUBSIZEU = []
PROG = []
PROK = []
PROP = []
Sad = []
Scg = []
AR = []
Sad.insert(0, 1)
indexmax = 0

if (ES == 1):
    SUBSIZE = int(input("Enter the  Size of subadders.\n"))
    indexmax = int(SIZE/SUBSIZE)
    for i in range(1, int(SIZE/SUBSIZE)):
        stindex = Sad[i-1] + SUBSIZE
        Sad.append(stindex)
    if (ECG == 1):
        CGSIZE = int(input("Enter the  Size of carry generator.\n"))
        for i in range(0, int(SIZE/SUBSIZE)):
            if (Sad[i]-CGSIZE < 0):
                Scg.append(0)
            else:
                cgstindex = Sad[i] - CGSIZE
                Scg.append(cgstindex)
    else:
        for i in range(0, int(SIZE/SUBSIZE)):
            CGSIZE = int(input("Enter the  Size of each carry generator.\n"))
            if (Sad[i]-CGSIZE < 0):
                Scg.append(0)
            else:
                cgstindex = Sad[i] - CGSIZE
                Scg.append(cgstindex)
    for i in range(0, int(SIZE/SUBSIZE)):
        PG = (1 / 2) - (1 / (2 ** (SUBSIZE + 1)))
        PP = 1 / (2 ** SUBSIZE)
        PROG.append(PG)
        PROK.append(PG)
        PROP.append(PP)
else:
    NOSUBADDERS = int(input("Enter the  number of subadders.\n"))
    indexmax = NOSUBADDERS
    for i in range(0, NOSUBADDERS):
        item = int(input("Enter the  Size of subadders.\n"))
        PG = (1/2)-(1/(2**(item+1)))
        PP = 1/(2**item)
        SUBSIZEU.append(item)
        PROG.append(PG)
        PROK.append(PG)
        PROP.append(PP)
    for i in range(1, NOSUBADDERS):
        stindex = Sad[i-1]+SUBSIZEU[i-1]
        Sad.append(stindex)
    if (ECG == 1):
        CGSIZE = int(input("Enter the  Size of carry generator.\n"))
        for i in range(0, NOSUBADDERS):
            if (Sad[i]-CGSIZE < 0):
                Scg.append(0)
            else:
                cgstindex = Sad[i] - CGSIZE
                Scg.append(cgstindex)
    else:
        for i in range(0, NOSUBADDERS):
            CGSIZE = int(input("Enter the  Size of each carry generator.\n"))
            if (Sad[i]-CGSIZE < 0):
                Scg.append(0)
            else:
                cgstindex = Sad[i] - CGSIZE
                Scg.append(cgstindex)
# Perr = 0
# PRint = 1
PAR = 1
for i in range(0, indexmax):
    ti = 0
    if (Scg[i] == 0):
        AR.insert(i, 1)
    else:
        for j in range(i, -1, -1):
            if (Sad[j] == Scg[i]):
                FTM = SUMTERM(j, i-1, PROG, PROP)
                STM = SUMTERM(0, i-1, PROK, PROP)
                TTM = 0.5*PRODP(0, i-1, PROP)
                AR.insert(i, FTM+STM+TTM)
            else:
                if (Sad[j] > Scg[i] > Sad[j-1]):
                    ti = i-j+1
                    FTM = SUMTERM(i-ti+1, i-1, PROG, PROP)
                    STM = SUMTERM(i-ti+1, i-1, PROK, PROP)
                    FFTM = SUMTERM(0, i-ti-1, PROK, PROP)
                    STTM = 0.5 * PRODP(0, i - 1, PROP)
                    TFTM = (1-(1/(2**(Sad[j]-Scg[i]+1)))) * \
                        PRODP(i-ti+1, i-1, PROP)
                    FTTM = ((1/2) - (1/(2**(Sad[j]-Scg[i]+2)))) * \
                        (1/(2**(Scg[i]-Sad[j-1]+1)))*PRODP(i-ti+1, i-1, PROP)
                    AR.insert(i, FTM+STM+FFTM+STTM+TFTM+FTTM)
    PAR = PAR*AR[i]
    # PAR = PAR + ((-1) ** i)* AR[i]
    # for j in range(0, comb(indexmax, i)):
    #     PRint = PRint * (1 - AR[i])
    #     print(PRint)
    #     Perr = Perr + ((-1) ** (i + 1)) * PRint

ER = 1-PAR


print(SUBSIZEU)
print(PROG)
print(PROK)
print(PROP)
print(Sad)
print(Scg)
print(AR)
print(PAR)
print(ER)
# print(Perr)

ri = []  # set of all prediction bits
ru = []  # union of prediction bits
gi = []  # set of all generation bits
# gu = []
gI = [] # intersection of all gi sets
gD = [] # difference set

for i in range(len(Sad)):
    # In each iteration, add an empty list to the main list
    ri.append([])

for i in range(len(Sad)):
    # In each iteration, add an empty list to the main list
    gi.append([])

Pr_int = 0


def probabilityP(n):
    return 1 / (2 ** n)


def probabilityG0(n):
    return (2 ** n - 1) / (2 ** (n + 1))

# Steps 1, 2, 3, 4 of algorithm 2
for i in range(0, len(Scg)):
    for j in range(Scg[i], Sad[i]):
        if j != 0:
            ri[i].append(j)

        if j not in ru and j != 0:
            ru.append(j)

    print(len(ru))
    Pr_int = probabilityP(len(ru))

# Steps 5, 6, 7, 8, 9 of algorithm 2
for i in range(0, len(Scg)):
    for j in range(0, SIZE + 1):
        # if j not in gu and j not in Sad and j != 0:
        #     gu.append(j)

        if j != 0 and j < Sad[i] and j not in ru:
            # print(ru)
            gi[i].append(j)

            if j not in gI:
                gI.append(j)

    print(len(gI))
    Pr_int *= probabilityG0(len(gI))


        # if j not in gu:
        #     # gi[i].append(j)
        #     gi[i].append(j)
        #     print(i, j)

    # Pr_int = probabilityP(len(ri))

    # for j in range(Sad[i], SIZE + 1):
    #     if j not in Sad and j not in ri:
    #         gi[0].append(j)

    # Pr_int *= probabilityG0(len(gi))


print('ri: ', ri)
print('ru: ', ru)
print('gi: ', gi)
# print('gu: ', gu)
print('gI: ', gI)
print(Pr_int)
print(Scg)
print(Sad)
