def probabilityP(n):
    return 1 / (2 ** n)


def probabilityG0(n):
    return (2 ** n - 1) / (2 ** (n + 1))


def probability(L, R, S):
    PE = []
    PEintersection = []
    n = 0
    for i in range(0, L):
        n += R[i - 1] + S[i - 1]
        pei = probabilityP(R[i]) * probabilityG0(n)
        PE.append(pei)

    Perr = 0
    for i in range(0, L):
        Perr += PE[i]

    print(Perr)

    print(PE)
    return PE


# number of sub-adders
L = int(input("Enter number of sub-adders : "))

# read inputs from user to get R and S lists
R = list(map(int, input(
    "\nEnter the number of prediction bits for each sub-adder : ").strip().split()))[:L]
S = list(map(int, input(
    "\nEnter the number of result bits for each sub-adder : ").strip().split()))[:L]

probability(L, R, S)
