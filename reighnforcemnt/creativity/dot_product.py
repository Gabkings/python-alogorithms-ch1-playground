'''
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
'''

a = [2,3,4,5]
b = [2,3,4,5]

def dot_product_array(a, b): 
    '''
    return an array c of length n such 
    that c[i] = a[i] ∗ b[i], for i = 0,...,n−1. 
 
    :param a: int vector 
    :param b: int vector 
    :return: c[i] = a[i] ∗ b[i], for i = 0,...,n−1. 
    ''' 
    return sum([x*y for x,y in zip(a,b)]) 
 
def dot_product(a,b): 
    '''
    The dot product between two vectors is based 
    on the projection of one vector onto another. 
 
    :param a: int vector 
    :param b: int vector 
    :return: sum(a[i] ∗ b[i], for i = 0,...,n−1.) 
    '''
    return sum(dot_product_array(a,b))

print(dot_product_array(a,b))

