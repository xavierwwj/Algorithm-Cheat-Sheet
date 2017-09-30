#########################################
#########################################
#########################################
### LIST OF USEFUL ALGORITHMS TO NOTE ###
#########################################
#########################################
#########################################


#########################################
# Algorithm 1: Exploiting sorted order  #
#########################################
def inner_product(L1,L2):
    """
    Example: inner_product([["and",3],["of",2],["the",5]],
                           [["and",4],["in",1],["of",1],["this",2]]) = 14.0 
    """
    sum = 0.0
    i = 0
    j = 0
    while i<len(L1) and j<len(L2):
        # L1[i:] and L2[j:] yet to be processed
        if L1[i][0] == L2[j][0]:
            # both vectors have this word
            sum += L1[i][1] * L2[j][1]
            i += 1
            j += 1
        elif L1[i][0] < L2[j][0]:
            """
            This involves string comparison, compares char pairs one by one
            until a difference surfaces

            """
            # word L1[i][0] is in L1 but not L2
            i += 1
        else:
            # word L2[j][0] is in L2 but not L1
            j += 1
    return sum
