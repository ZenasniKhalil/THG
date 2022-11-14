import string


def get_matrix_header_letters(number_of_nodes):
    if number_of_nodes <= 26:
        alphabet = list(string.ascii_lowercase.upper())
    else:
        alphabet = []
        for i in range(1,number_of_nodes + 1):
          alphabet.append(str(i))
    return alphabet[0:number_of_nodes]



def get_empty_matrix(number_of_nodes):
    l = []
    n = number_of_nodes
    # We need a n by n matrix
    for i in range(0, n):
        l.append([])
        for j in range(0, n):
            l[i].append(0)
    return l