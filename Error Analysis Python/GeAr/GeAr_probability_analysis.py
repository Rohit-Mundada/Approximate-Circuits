# def error_probability(N, R, P):
#     L = R + P   # length of each sub-adder
#     k = int((N - L) / R) + 1   # total number of sub-adders
#     m = k - 1   # number of sub-adders that can contain error
#     Pr = 0.5    # propagate probability
#     Gr = 0.25   # generate probability

#     probability_error = 0
#     array_terms = []

#     for i in range(0, R):
#         probability_error += m * Gr * (Pr ** (P + i))

#     if m == 0:
#         probability_error = 0
#     elif m > 1:
#         index = 1
#         for i in range(1, m + 1):
#             for j in range(1, R + 1):
#                 array_terms[index].start = index
#                 array_terms[index].end = L + (i - 1) * R
#                 array_terms[index].prop = array_terms[index].end - \
#                     array_terms[index].start
#                 index += 1

#         max_index = m * R
#         remaining_probability_terms = 0
#         for i in range(1, max_index + 1):
#             end_index = array_terms[i].end
#             propagate_terms = array_terms[i].prop
#             generate_terms = 1
#             multiply_terms = -1
#             for j in range(i + 1, max_index + 1):
#                 if array_terms[j].start > end_index:
#                     generate_terms_temp = generate_terms + 1
#                     propagate_terms_temp = propagate_terms + array_terms[j].prop
#                     # end_index_temp = array_terms[i].end
#                     remaining_probability_terms = remaining_probability_terms + \
#                         (multiply_terms * (Gr ** generate_terms_temp)
#                         * (Pr ** propagate_terms_temp))
#                     # remaining_probability_terms =
            
#     return probability_error

# N = int(input("Enter the total size of the adder\n"))
# R = int(input("Enter the resultant bits to be used in each sub-adder\n"))
# P = int(input("Enter the prediction bits to be used in each sub-adder\n"))

# print("Probability of Error is: {0}".format(error_probability(N, R, P)))
# # for i in range(1, 10):
# #     print(i);


def Probability_Error(N, R, P):
    L = R + P
    k = (N - L) / R + 1
    Pr = 0.5
    Gr = 0.25

    prob_error_generating_events = []

    for m in range(1, R + 1):
        for s in range(1, k - 1):
            prob_error_generating_events[m + s * R] = Gr * (Pr ** (L - m))

    
    