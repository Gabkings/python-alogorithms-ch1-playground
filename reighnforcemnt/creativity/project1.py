def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False;
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))

'''
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
'''

def odd_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product & 1:
          return True
          return False
          
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
print(dt1, odd_product(dt1))
print(dt2, odd_product(dt2))


def demonstration_list_comprehension(): 
    '''Python List comprehension demonstration 
 
    :return: [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] 
    ''' 
    return [idx * x for idx, x in enumerate(range(1,11))]

print(demonstration_list_comprehension())


def demonstration_list_comprehension_abc(): 
    ''' Python list comprehension demonstration 
 
    :return: 
     [’a’, ’b’, ’c’, ’d’, ’e’, ’f’, ’g’, ’h’, 
     ’i’, ’j’, ’k’, ’l’, ’m’, ’n’, ’o’, ’p’, 
     ’q’, ’r’, ’s’, ’t’, ’u’, ’v’, ’w’, ’x’, 
     ’y’, ’z’] 
    ''' 
    return [chr(x) for x in range(ord('a'), ord('z')+1)]

print(demonstration_list_comprehension_abc())


'''
Python’s random module includes a function shuffle(data) that accepts a 
list of elements and randomly reorders the elements so that each possi− 
ble order occurs with equal probability. The random module includes a 
more basic function randint(a, b) that returns a uniformly random integer 
from a to b (including both endpoints). Using only the randint function, 
implement your own version of the shuffle function. 
'''

def sub_shuffle(data, indexlist): 
    import random 
    index = random.randint(0, len(indexlist) - 1) 
    rElement = data[indexlist[index]] 
    indexlist.pop(index) 
    return rElement 
 
def custome_shuffle(data): 
    indexes_of_data = range(len(data)) 
    return [sub_shuffle(data, indexes_of_data) for e in range(len(data))]


#print(custome_shuffle([1,2,3,4,5,6]))

