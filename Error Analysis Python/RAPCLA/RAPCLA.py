import os
import numpy as np
from matplotlib import pyplot as plt
import pandas
from pandas import Series
import random
import array
import csv
import itertools

get_bin = lambda x, n: format(x, 'b').zfill(n)

def BIT_G(A, B):
    BIT_GEN = A & B
    return BIT_GEN


def BIT_P(A, B):
    BIT_PROP =  bin(int(A,2) ^ int(B,2))
    return BIT_PROP

def BC(g, p, valency):
    gg=g
    gp=p
    gg[0] = g[0]
    gp[0] = p[0]

    for i in range(0, valency-1):
        gg[i+1] = g[i+1]|(gg[i]&p[i+1])
        gp[i+1] = p[i+1] & gp[i]
    return gg[valency-1],gp[valency-1]

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

def RAPCLA_p(a, b, Cin, ApproxCON, SIZE, groupsize, window):
    g = []
    g.insert(0,0)
    p = []
    p.insert(0,0)
    GG1 = []
    GG1.insert(0,0)
    GP1 = []
    GP1.insert(0,0)
    SUM = []
    AR = get_bin(a, SIZE)
    BR = get_bin(b, SIZE)
    #Cin = get_bin(C,1)
    #print(int(Cin[0],2))
    A = AR[::-1]
    B = BR[::-1]
    ApproxRCONR = get_bin(ApproxCON,int(SIZE/groupsize))
    ApproxRCON = ApproxRCONR[::-1]
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
    GE = []
    #GGR = []
    GG.insert(0,Cin)
    #GE.insert(0, 0)
    #print(GE)
    #GG.insert(1,1)
    for i in range(0, int(SIZE/groupsize)):
        X, Y = BC(g[i*groupsize+1:(i+1)*groupsize-window+1], p[i*groupsize+1:(i+1)*groupsize-window+1], groupsize - window)
        GG1.insert(i*2+1, X)
        GP1.insert(i*2+1, Y)
        X, Y = BC(g[(i+1)*groupsize-window+1:(i+1)*groupsize+1], p[(i+1)*groupsize-window+1:(i+1)*groupsize+1], window)
        GG1.insert(i*2+2, X)
        GP1.insert(i*2+2, Y)
        for j in range(0, groupsize-window-1):
            P =  GC(list(GG[i*groupsize+j:i*groupsize+j+1])+list(g[i*groupsize+j+1:i*groupsize+j+2]),list([0])+list(p[i*groupsize+j+1:i*groupsize+j+2]),2)
            GG.insert(i*groupsize+j+1, P)
        M = GC(list(GG[i*groupsize:i*groupsize+1])+list(GG1[i*2+1:i*2+2]),list([0])+list(GP1[i*2+1:i*2+2]),2)
        GG.insert((i+1)*groupsize-window, M)
        for j in range(0, window-1):
            Q =  GC(list(GG[(i+1)*groupsize-window+j:(i+1)*groupsize-window+j+1])+list(g[(i+1)*groupsize-window+j+1:(i+1)*groupsize-window+j+2]),list([0])+list(p[(i+1)*groupsize-window+j+1:(i+1)*groupsize-window+j+2]),2)
            GG.insert((i+1)*groupsize-window+j+1, Q)
        N = GC(list(GG[(i+1)*groupsize-window:(i+1)*groupsize-window+1])+list(GG1[i*2+2:i*2+3]),list([0])+list(GP1[i*2+2:i*2+3]),2)
        GE.insert(i, N)

        O = MUX_2_1(GG1[i*2+2], GE[i], int(ApproxRCON[i]))
        GG.insert((i+1)*groupsize, O)

    for i in range(0, SIZE):
        S = p[i+1] ^ GG[i]
        SUM.insert(i,S)
    SUM.insert(SIZE,GG[SIZE])
    SUMR = SUM[::-1]
    SUMINTR = int("".join(str(x) for x in SUMR), 2)

    return SUMINTR






#*************************************************************************************************


groupsize = int(input("Enter the  groupsize.\n"))
window =  int(input("Enter the  size of window.\n"))
ReConCode = int(input("Enter code 1 for Approximate mode, 2 for Half Approximate mode and 3 for exact mode.\n"))


X = list(map(int, input("Enter different size values  of adder seperated by blank space and press enter\n").split()))

curr_dict = os.getcwd()
dir_name = "RAPCLA_ERROR_ANALYSIS"
path_name = os.path.join(curr_dict, dir_name)

if dir_name not in os.listdir():
    os.mkdir(path_name)

filename1 = "groupsize{0}_window{1}_Mode{2}.csv".format(groupsize, window, ReConCode)
filename2 = "groupsize{0}_window{1}_Mode{2}_transposed.csv".format(groupsize, window, ReConCode)

with open(os.path.join(path_name, filename1), 'w') as newFile1:
    newFileWriter = csv.writer(newFile1)
    newFileWriter.writerow(["SIZE","error_rate", "Average_Error", "Acceptance_Probability", "HDP", "MRED", "NMED"])

for i in range(0, len(X)):
    SIZE = X[i]
    if ReConCode == 1:
        ApproxRCON = 2**int(SIZE/groupsize) - 1
    elif  ReConCode == 2:
        ApproxRCON = 2**int(SIZE/(groupsize*2)) - 1
        print(ApproxRCON)
    else:
        ApproxRCON = 0
        print(ApproxRCON)

    iterations = 1000000
    errorcount = 0
    Maximum_Error = 0
    Total_Error = 0
    Average_Error = 0
    Average_Error_Max = 0
    A_Max = 0
    B_Max = 0
    Acceptance = 0
    BIT_Flip_Error_Max = 0
    Total_BIT_Flip_Error = 0
    NMED_total = 0
    Hamming_distance = 0


    for i in range(0, iterations):
        # generate a, b and c randomly
        a = random.randint(0,2**SIZE-1)
        b = random.randint(0, 2 ** SIZE - 1)
        c = random.randint(0,1)

        # calculate exact and approximate sum
        EXACT_SUM = a + b + c
        APPROX_SUM = RAPCLA_p(a, b, c, ApproxRCON, SIZE, groupsize, window)
        #print(a,b,c,EXACT_SUM, APPROX_SUM)
        # if error :
        if  (EXACT_SUM != APPROX_SUM):
            errorcount = errorcount+1
            absolute_error = abs(EXACT_SUM-APPROX_SUM)
            if absolute_error > Maximum_Error:
                Maximum_Error = absolute_error
            Total_Error = Total_Error + absolute_error
            Average_Error = Average_Error + (absolute_error/EXACT_SUM)
            NMED_total = NMED_total + (absolute_error/(2**SIZE-1))
            if (absolute_error/EXACT_SUM) > Average_Error_Max:
                Average_Error_Max = (absolute_error/EXACT_SUM)
                A_Max = a
                B_Max = b
        if EXACT_SUM != 0:
            if (EXACT_SUM - APPROX_SUM)/EXACT_SUM < 0.001:
                Acceptance = Acceptance + 1
        else:
            Acceptance = Acceptance + 1

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
        Hamming_distance = Hamming_distance + (BIT_Flip_Error/SIZE)


    HDP = "{0:.3f}".format(100*Hamming_distance/iterations)
    MRED = "{0:.3f}".format(100*Average_Error/iterations)
    NMED = "{0:.3f}".format(100*NMED_total/iterations)
    error_rate = "{0:.2f}".format(100*errorcount/iterations)
    Acceptance_Probability = "{0:.3f}".format(100*Acceptance/iterations)
#*************************************************************************
# Results to be written in file
#*************************************************************************



    # open file for write access
    filename = "SIZE{0}_groupsize{1}_window{2}_Mode{3}.txt".format(SIZE, groupsize, window, ReConCode)
    filename1 = "groupsize{0}_window{1}_Mode{2}.csv".format(groupsize, window, ReConCode)
    file = open(os.path.join(path_name, filename), "w")

    # write into file : heading and parameters
    file.write("RAPCLA ERROR ANALYSIS\n\n")
    file.write("Parameters :\n")
    file.write("\tSIZE = {0}\n".format(SIZE))
    file.write("\tgroupsize = {0}\n".format(groupsize))
    file.write("\tWindow Size = {0}\n".format(window))

# write stats into file for chosen error attributes

    file.write("\nNumber of iterations\t: {0}\n".format(iterations))
    file.write("Number of error cases\t: {0}\n".format(errorcount))
    file.write("Error Rate = errorcount/no. of iterations\n\t")
    file.write("={0}\n".format(error_rate))

    file.write("Maximum Hamming Distance = {0}\n".format(BIT_Flip_Error_Max))
    file.write("Average Hamming Distance = Total_BIT_Flip_Error / iterations\n\t")
    file.write("= {0:.3f} (Over all iterations)\n\t".format(Total_BIT_Flip_Error/iterations))
    if errorcount != 0:
        file.write("= {0:.3f} (Over erroneous iterations)\n\n".format(Total_BIT_Flip_Error/errorcount))

    file.write("Maximum Error = {0} (Absolute value)\n".format(Maximum_Error))
    file.write("Average error(Error_Distance)(sum of errors/iterations) = {0} \n\t".format(Average_Error))
    if errorcount != 0:
        file.write("= {0:.3f} (Over erroneous iterations)\n\n".format(Total_Error/errorcount))
    file.write("Average Maximum Error = {0} \n\n".format(Average_Error_Max))

    file.write("Acceptance Probability Over iterations\n\t")
    file.write("={0} (in %) \n\n".format(Acceptance_Probability))


    with open(os.path.join(path_name, filename1), 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow([SIZE, error_rate, "{0:.3f}".format(Average_Error), Acceptance_Probability, HDP, MRED, NMED])


a = zip(*csv.reader(open(os.path.join(path_name, filename1), "r")))
csv.writer(open(os.path.join(path_name, filename2), "w")).writerows(a)








