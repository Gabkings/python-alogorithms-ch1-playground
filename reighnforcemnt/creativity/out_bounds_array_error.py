def catch_array_out_of_bounds(): 
    '''
    Exception catching example 
 
    :return: doesn’t return 
    ''' 
    try: 
        l = [] 
        l[0] = 1 
    except IndexError as ex: 
        print("Don’t try buffer overflow attacks in Python!")

catch_array_out_of_bounds()