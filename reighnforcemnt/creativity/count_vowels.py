def count_vowels(word): 
    '''
    counts the number of vowels in a given 
    character string. 
 
    :param word: String in which 
    to search vowels 
    :return: a Dictionary with the vowel and 
    times appeared 
    {’a’: #, ’i’: #, ’e’: #, ’u’: #, ’o’: #} 
    ''' 
    counts = {}.fromkeys("aeiou", 0) 
    for char in word.lower(): 
        if char in counts: 
            counts[char] += 1 
    return counts

print(count_vowels('sjaouwuqiwwbdiuucbfwf'))