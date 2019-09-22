def sqauares_sum(n):
    return sum([k*k for k in range(1,n)])

print(sqauares_sum(20))

def sum_of_squares_odd(n):
    return sum([k*k for k in range(1,n) if k % 2 != 0])

print(sum_of_squares_odd(5))


#indeces equivalence 

def same_index():
    s = "pythonstring"
    n = len(s)

    for k in range(-n, 0):
        print(s[k])


    for j in range(-n, 0):
        print(s[j + n])

#same_index()

'''
Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
'''
print([pow(2, k) for k in range(0, 9, +1)])

# Write a pseudo-code description of a function that reverses a list of n integers,
# so that the numbers are listed in the opposite order than they were before, and compare
# this method to an equivalent Python function for doing the same thing.

mylist = [1,2,3,4,5,6,7,8,9]

def list_reverse(data):
    temp = []
    n = len(data) - 1
    for thing in range(n, -1, -1):
        temp.append(data[thing])
    return temp

print(mylist)
print(list_reverse(mylist))

