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

#############################################
# Algorithm 2: Dealing with key-value pairs #
#############################################
def count_frequency(word_list):
    """
    Using a dictionary over a list is always favourable
    for the fact that you can search if key is in dict
    at O(1) rather than having to look through an entire
    list at O(n) efficiency.

    word_list - [word1, word2 ...]
    return - {word: freq, ...}
    """
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    return D.items()

###########################
# Algorithm 3: Merge Sort #
###########################

"""
1) Iterative has space complexity of O(1) whereas recursive has
that of O(n)
2) Time complexity - O(nlog(n))
3) Space complexity - O(n) for arrays i.e. lists in python, O(log(n))
for linked lists, where n = number of elements in input.

Reasons:
a) max stack depth = log(n). For arrays, for the k'th depth excluding
first level, no. of elements = n/2^k. As such, sum = n + n/2 + ....
Asymptotically, the space complexity reaches 2n and thus O(n).
b) For linked lists, the stack size per depth is constant, so clog(n)
gives O(log(n)).
"""
def merge_sort(A):
    """
    Sort list A into order, and return result.
    """
    n = len(A)
    if n==1: 
        return A
    mid = n//2     # floor division
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L,R)

def merge(L,R):
    """
    Given two sorted sequences L and R, return their merge.
    """
    i = 0
    j = 0
    answer = []
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            answer.append(L[i])
            i += 1
        else:
            answer.append(R[j])
            j += 1
    if i<len(L):
        answer.extend(L[i:])
    if j<len(R):
        answer.extend(R[j:])
    return answer

############################
# Algorithm 4: Memoisation #
############################
"""
Reference: https://www.python-course.eu/python3_memoization.php
"""
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(40))


#######################################
# Code Choice 1: String concatenation #
#######################################
"""AVOID THIS"""
s = ""
for substring in list:
    s += substring

"""DO THIS"""
slist = [some_function(elt) for elt in somelist]
s = "".join(slist)


"""AVOID THIS"""
out = "<html>" + head + prologue + query + tail + "</html>"

"""DO THIS"""
out = "<html>%s%s%s%s</html>" % (head, prologue, query, tail)

###################################
# Code Choice 2: String splitting #
###################################
translation_table = string.maketrans(string.punctuation+string.uppercase,
                                     " "*len(string.punctuation)+string.lowercase)

def get_words_from_string(line):
    """
    Input:  line (a string)
    Output: a list of strings 
              (each string is a sequence of alphanumeric characters)
    """
    line = line.translate(translation_table)
    word_list = line.split()
    return word_list
