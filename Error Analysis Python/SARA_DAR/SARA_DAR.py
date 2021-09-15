import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas import Series
import random
import array

get_bin = lambda x, n: format(x, 'b').zfill(n)

def BIT_G(A, B):
    BIT_GEN = A & B
    return BIT_GEN


def BIT_P(A, B):
    BIT_PROP =  bin(int(A,2) ^ int(B,2))
    return BIT_PROP



def GC(g, p, valency):
    gg=g
    gp=p
    gg[0] = g[0]
    gp[0] = p[0]

    for i in range(0, valency-1):
        gg[i+1] = g[i+1]|(gg[i]&p[i+1])
    return gg[valency-1]

def MUX_2_1(A, B, sel):
    if sel == 1:
        return A
    else:
        return B

def SARA_DAR_p(a, b, Cin, SIZE, groupsize, window, carryoutselect):
    g = []
    g.insert(0,0)
    p = []
    p.insert(0,0)

    SUM = []
    AR = get_bin(a, SIZE)
    BR = get_bin(b, SIZE)
    #Cin = get_bin(C,1)
    #print(int(Cin[0],2))
    A = AR[::-1]
    B = BR[::-1]

    #print(A)
    #print(B)
    #print(ApproxRCON)
    for i in range(0, SIZE):
        #a_i = int(A & (1 << i) > 0)
        #b_i = int(B & (1 << i) > 0)
        g = g + [int(A[i],2) * int(B[i],2)]
        p = p + [int(A[i],2) ^ int(B[i],2)]

    #print(g)
    #print(p)

    GG = []
    groupcarryout = []
    GE = []
    #GGR = []
    GG.insert(0,Cin)
    groupcarryout.insert(0, Cin)

    ApproxRCON = []
    #GE.insert(0, 0)
    #print(GE)
    #GG.insert(1,1)
    for i in range(0, int(SIZE/groupsize)-1):
        X =  GC(list(list(groupcarryout[i:i+1]+g[i*groupsize+1:i*groupsize+2])),list([0])+list(p[i*groupsize+1:i*groupsize+2]),2)
        GG.insert(i*groupsize+1, X)
        for j in range(0, groupsize-1):
            P =  GC(list(GG[i*groupsize+j+1:i*groupsize+j+2])+list(g[i*groupsize+j+2:i*groupsize+j+3]),list([0])+list(p[i*groupsize+j+2:i*groupsize+j+3]),2)
            GG.insert(i*groupsize+j+2, P)
        Q = int(p[(i+1)*groupsize+2]) &  int(p[(i+1)*groupsize+1])
        ApproxRCON.insert(i*(window-1),Q)
        for j in range(0, window-2):
            R = int(p[(i+1)*groupsize+j+3]) & int(ApproxRCON[i*(window-1)+j])
            ApproxRCON.insert(i*(window-1)+j+1, R)
        O = MUX_2_1(g[(i+1)*groupsize], GG[(i+1)*groupsize], int(ApproxRCON[i*(window-1)+window-2]))
        groupcarryout.insert(i+1, O)
    Y =  GC(list(groupcarryout[int(SIZE/groupsize)-1:int(SIZE/groupsize)])+list(g[SIZE-groupsize+1:SIZE-groupsize+2]),list([0])+list(p[SIZE-groupsize+1:SIZE-groupsize+2]),2)
    GG.insert(SIZE-groupsize+1, Y)
    for j in range(0, groupsize-1):
        Z =  GC(list(GG[SIZE-groupsize+j+1:SIZE-groupsize+j+2])+list(g[SIZE-groupsize+j+2:SIZE-groupsize+j+3]),list([0])+list(p[SIZE-groupsize+j+2:SIZE-groupsize+j+3]),2)
        GG.insert(SIZE-groupsize+j+2, Z)
    M = MUX_2_1(g[SIZE], GG[SIZE], int(carryoutselect))
    groupcarryout.insert(int(SIZE/groupsize), M)
    for i in range(0, SIZE):
        S = p[i+1] ^ GG[i]
        SUM.insert(i,S)
    SUM.insert(SIZE,groupcarryout[int(SIZE/groupsize)])
    SUMR = SUM[::-1]

    SUMINTR = int("".join(str(x) for x in SUMR), 2)

    return SUMINTR






#*************************************************************************************************

SIZE = int(input("Enter the total size of adder\n"))
groupsize = int(input("Enter the  groupsize.\n"))
window =  int(input("Enter the  window size.\n"))
carryoutselect = int(input("Enter the  carryoutselect for final carry.\n"))


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
    a = random.randint(0,2**SIZE-1)
    b = random.randint(0, 2 ** SIZE - 1)
    c = random.randint(0,1)

    # calculate exact and approximate sum
    EXACT_SUM = a + b + c

    APPROX_SUM = SARA_DAR_p(a, b, c, SIZE, groupsize, window, carryoutselect)
    #print(a,b,c,EXACT_SUM, APPROX_SUM)
    # if error :
    if  (EXACT_SUM != APPROX_SUM):
       errorcount = errorcount+1
       absolute_error = abs(EXACT_SUM-APPROX_SUM)
       if absolute_error > Maximum_Error:
            Maximum_Error = absolute_error
       Total_Error = Total_Error + absolute_error
       Average_Error = Average_Error + (absolute_error/EXACT_SUM)
       if (absolute_error/EXACT_SUM) > Average_Error_Max:
            Average_Error_Max = (absolute_error/EXACT_SUM)
            A_Max = a
            B_Max = b
    if (EXACT_SUM - APPROX_SUM)/EXACT_SUM < 0.01:
        Acceptance_Probability =Acceptance_Probability + 1

    EXACT_SUM_BR = get_bin(EXACT_SUM, SIZE+1)
    EXACT_SUM_B = EXACT_SUM_BR[::-1]

    APPROX_SUM_BR = get_bin(APPROX_SUM, SIZE+1)
    APPROX_SUM_B = APPROX_SUM_BR[::-1]

    BIT_Flip_Error = 0

    for i in range(0, SIZE+1):
        if int(APPROX_SUM_B[i]) != int(EXACT_SUM_B[i]):
            BIT_Flip_Error = BIT_Flip_Error +1
        if BIT_Flip_Error > BIT_Flip_Error_Max:
            BIT_Flip_Error_Max = BIT_Flip_Error
    Total_BIT_Flip_Error = Total_BIT_Flip_Error + BIT_Flip_Error


#*************************************************************************
# Results to be written in file
#*************************************************************************

curr_dict = os.getcwd()
dir_name = "SARA_DAR_ERROR_ANALYSIS"
path_name = os.path.join(curr_dict, dir_name)

if dir_name not in os.listdir():
    os.mkdir(path_name)

# open file for write access
filename = "SIZE{0}_groupsize{1}_window{2}.txt".format(SIZE, groupsize, window)
file = open(os.path.join(path_name, filename), "w")

# write into file : heading and parameters
file.write("SARA_DAR ERROR ANALYSIS\n\n")
file.write("Parameters :\n")
file.write("\tSIZE = {0}\n".format(SIZE))
file.write("\tgroupsize = {0}\n".format(groupsize))
file.write("\twindow = {0}\n".format(window))
file.write("\tFinal carry select carryoutselect = {0}\n".format(carryoutselect))



# write stats into file for chosen error attributes

file.write("\nNumber of iterations\t: {0}\n".format(iterations))
file.write("Number of error cases\t: {0}\n".format(errorcount))
file.write("Error Rate = errorcount/no. of iterations\n\t")
file.write("= {0:.3f}%\n\n".format((100*errorcount/iterations)))

file.write("Maximum Hamming Distance = {0}\n".format(BIT_Flip_Error_Max))
file.write("Average Hamming Distance = Total_BIT_Flip_Error / iterations\n\t")
file.write("= {0:.3f} (Over all iterations)\n\t".format(Total_BIT_Flip_Error/iterations))
if errorcount != 0:
    file.write("= {0:.3f} (Over erroneous iterations)\n\n".format(Total_BIT_Flip_Error/errorcount))

file.write("Maximum Error = {0} (Absolute value)\n".format(Maximum_Error))
file.write("Average error(sum of errors/iterations) = {0} \n\t".format(Average_Error))
if errorcount != 0:
    file.write("= {0:.3f} (Over erroneous iterations)\n\n".format(Total_Error/errorcount))
file.write("Average Maximum Error = {0} \n\n".format(Average_Error_Max))

file.write("Acceptance Probability Over iterations\n\t")
file.write("= {0:.3f}  (in %) \n\n".format(100*Acceptance_Probability/iterations))








