import math 
 
def nroot(x, n): 
    '''
    Calculates the root to a given 
    radical n 
 
    :param x: number to which we want to find 
     root to n radical 
    :param n: radical 
    :return: the root 
    '''
    return int(math.pow(x, 1.0/n)) 
 
def norm(v, p=2): 
    '''The p−norm of a vector v 
 
    :param v: a vector of integers 
    :param p: radical of the root 
    :return: p−norm of a vector v 
    '''
    return nroot(sum(list(map((lambda x: x **p), v))), p)


print(norm([4,3]))