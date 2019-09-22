
import operator 
def ordered_integers(a,b,c):  
    '''
    determines if the arguments can be used 
    in a correct arithmetic formula (in the given 
    order), like ”a+b = c,” ”a = b−c,” or ”a∗b = c.” 
 
    :param a: integer 
    :param b: integer 
    :param c: integer 
    :return: list with operation names that 
    give correct arithmetic formula 
    '''
    operator_list = [operator.add, operator.sub, 
                     operator.mul, operator.div] 
    result_list = list() 
    for op in operator_list: 
        if a == op(float(b),float(c)): 
            result_list.append(op.__name__) 
        if c == op(float(a),float(b)): 
            result_list.append(op.__name__) 
    return result_list

ordered_integers(1,2,3)