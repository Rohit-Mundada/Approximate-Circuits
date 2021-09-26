import os
import numpy as np
# from matplotlib import pyplot as plt
import pandas as pd
from pandas import Series
import random
import array
import math


def get_bin(x, n): return format(x, 'b').zfill(n)


def BIT_G(A, B): return A & B


def BIT_P(A, B): return bin(int(A, 2) ^ int(B, 2))


def BC(g, p, valency):
    gg = g
    gp = p
    gg[0] = g[0]
    gp[0] = p[0]

    for i in range(0, valency - 1):
        gg[i + 1] = g[i + 1] | (gg[i] & p[i + 1])
        gp[i + 1] = p[i + 1] & gp[i]
    return gg[valency - 1], gp[valency - 1]


def GC(g, p, valency):
    gg = g
    gp = p
    gg[0] = g[0]
    gp[0] = p[0]

    for i in range(0, valency - 1):
        gg[i + 1] = g[i + 1] | (gg[i] & p[i + 1])
    return gg[valency - 1]


def MUX_2_1(A, B, sel):
    if sel == 1:
        return A
    else:
        return B


def CLA_p(A, B, Cin, SIZE, valency):
    g = []
    g.insert(0, 0)
    p = []
    p.insert(0, 0)
    GG1 = []
    GG1.insert(0, 0)
    GP1 = []
    GP1.insert(0, 0)
    SUM = []

    for i in range(0, SIZE):
        # a_i = int(A & (1 << i) > 0)
        # b_i = int(B & (1 << i) > 0)
        g = g + [int(A[i], 2) * int(B[i], 2)]
        p = p + [int(A[i], 2) ^ int(B[i], 2)]

    GG = []

    GG.insert(0, Cin)

    for i in range(0, int(SIZE / valency)):
        X, Y = BC(g[valency * i + 1:(i + 1) * valency + 1],
                  p[valency * i + 1:(i + 1) * valency + 1], valency)
        GG1.insert(i + 1, X)
        GP1.insert(i + 1, Y)
        for j in range(0, valency - 1):
            L = GC(list(GG[i * valency + j:i * valency + j + 1]) + list(g[i * valency + j + 1:i * valency + j + 2]),
                   list([0]) + list(p[i * valency + j + 1:i * valency + j + 2]), 2)
            GG.insert(i * valency + j + 1, L)
        Z = GC(list(GG[i * valency:i * valency + 1]) +
               list(GG1[i + 1:i + 2]), list([0]) + list(GP1[i + 1:i + 2]), 2)
        GG.insert((i + 1) * valency, Z)
    for i in range(0, SIZE):
        S = p[i + 1] ^ GG[i]
        SUM.insert(i, S)

        # SUMINTR = int("".join(str(x) for x in SUMR), 2)

    return SUM, GG[SIZE]


def GeAr_p(a, b, Cin, N, R, P, valency):
    AR = get_bin(a, N)
    BR = get_bin(b, N)
    # Cin = get_bin(C,1)
    # print(int(Cin[0],2))
    A = AR[::-1]
    B = BR[::-1]
    cout = []
    SUM = []

    x, y = CLA_p(A[0:R + P], B[0:R + P], Cin, R + P, valency)
    SUM.extend(x)
    cout.append(y)
    for j in range(1, int((N - R - P) / R) + 1):
        z, l = CLA_p(A[j * R:(j + 1) * R + P],
                     B[j * R:(j + 1) * R + P], 0, R + P, valency)
        SUM.extend(z[P:R + P])
        cout.append(l)
    SUM.insert(N, cout[len(cout) - 1])
    SUMR = SUM[::-1]
    SUMINTR = int("".join(str(x) for x in SUMR), 2)
    return SUMINTR


# *************************************************************************************************


N = int(input("enter the total size of adder\n"))
R = int(input("enter the  number of result bits from each subadder.\n"))
P = int(input("enter the  number of prediction bits for each subadder.\n"))
valency = int(input("Enter valency to be used in each subadder.\n"))

print("Result is: {0}"
      .format(
          hex(
              GeAr_p(
                  int("A5C3", 16),
                  int("CA53", 16),
                  0,
                  N,
                  R,
                  P,
                  valency
              )
          )
      )
      )

iterations = 100000
errorcount = 0
Maximum_Error = 0
Total_Error = 0
Average_Error = 0
Average_Error_Max = 0
A_Max = 0
B_Max = 0
Acceptance_Probability = 0
BIT_Flip_Error_Max = 0
Total_BIT_Flip_Error = 0

for i in range(0, iterations):
    # generate a, b and c randomly
    a = random.randint(0, 2 ** N - 1)
    b = random.randint(0, 2 ** N - 1)
    c = random.randint(0, 1)
    # a = i + 1
    # b = math.floor(iterations / 2)
    # c = 0

    # calculate exact and approximate sum
    EXACT_SUM = a + b + c
    APPROX_SUM = GeAr_p(a, b, c, N, R, P, valency)

    # print(a,b,c,EXACT_SUM, APPROX_SUM)
    # if error :
    if (EXACT_SUM != APPROX_SUM):
        errorcount = errorcount + 1
        absolute_error = abs(EXACT_SUM - APPROX_SUM)
        if absolute_error > Maximum_Error:
            Maximum_Error = absolute_error
        Total_Error = Total_Error + absolute_error
        Average_Error = Average_Error + (absolute_error / EXACT_SUM)
        if (absolute_error / EXACT_SUM) > Average_Error_Max:
            Average_Error_Max = (absolute_error / EXACT_SUM)
            A_Max = a
            B_Max = b
    if (EXACT_SUM - APPROX_SUM) / EXACT_SUM < 0.01:
        Acceptance_Probability = Acceptance_Probability + 1

    EXACT_SUM_BR = get_bin(EXACT_SUM, N + 1)
    EXACT_SUM_B = EXACT_SUM_BR[::-1]

    APPROX_SUM_BR = get_bin(APPROX_SUM, N + 1)
    APPROX_SUM_B = APPROX_SUM_BR[::-1]

    BIT_Flip_Error = 0

    for i in range(0, N + 1):
        if int(APPROX_SUM_B[i]) != int(EXACT_SUM_B[i]):
            BIT_Flip_Error = BIT_Flip_Error + 1
        if BIT_Flip_Error > BIT_Flip_Error_Max:
            BIT_Flip_Error_Max = BIT_Flip_Error
    Total_BIT_Flip_Error = Total_BIT_Flip_Error + BIT_Flip_Error

# *************************************************************************
# Results to be written in file
# *************************************************************************

curr_dict = os.getcwd()
dir_name = "GeAr_ERROR_ANALYSIS"
path_name = os.path.join(curr_dict, dir_name)

if dir_name not in os.listdir():
    os.mkdir(path_name)

# open file for write access
filename = "N{0}_R{1}_P{2}_valency{3}.txt".format(N, R, P, valency)
file = open(os.path.join(path_name, filename), "w")

# write into file : heading and parameters
file.write("GeAr ERROR ANALYSIS\n\n")
file.write("Parameters :\n")
file.write("\tN = {0}\n".format(N))
file.write("\tR = {0}\n".format(R))
file.write("\tP = {0}\n".format(P))
file.write("\tvalency = {0}\n".format(valency))

# write stats into file for chosen error attributes

file.write("\nNumber of iterations\t: {0}\n".format(iterations))
file.write("Number of error cases\t: {0}\n".format(errorcount))
file.write("Error Rate = errorcount/no. of iterations\n\t")
file.write("= {0:.3f}%\n\n".format((100 * errorcount / iterations)))

file.write("Maximum Hamming Distance = {0}\n".format(BIT_Flip_Error_Max))
file.write("Average Hamming Distance = Total_BIT_Flip_Error / iterations\n\t")
file.write("= {0:.3f} (Over all iterations)\n\t".format(
    Total_BIT_Flip_Error / iterations))
if errorcount != 0:
    file.write("= {0:.3f} (Over erroneous iterations)\n\n".format(
        Total_BIT_Flip_Error / errorcount))

file.write("Maximum Error = {0} (Absolute value)\n".format(Maximum_Error))
file.write(
    "Average error(sum of errors/iterations) = {0} \n\t".format(Average_Error))
if errorcount != 0:
    file.write("= {0:.3f} (Over erroneous iterations)\n\n".format(
        Total_Error / errorcount))
file.write("Average Maximum Error = {0} \n\n".format(Average_Error_Max))

file.write("Acceptance Probability Over iterations\n\t")
file.write("= {0:.3f}  (in %) \n\n".format(
    100 * Acceptance_Probability / iterations))
