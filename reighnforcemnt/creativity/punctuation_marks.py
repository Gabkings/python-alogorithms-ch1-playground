def strip_string(sentence): 
    '''
    returns a copy of the string with all punctuation removed 
 
    :param sentence: source sentence in string form 
    :return: string without ’,.;:?!−_()[]∖’∖”‘/<>{}#=’ 
    ''' 
    punctuation_marks = r',.;:?!−_()[]∖’∖”‘/<>{}#='
    for punctuation in punctuation_marks: 
        sentence = sentence.replace(punctuation, "") 
    return sentence

print(strip_string("Let's try, Mike."))