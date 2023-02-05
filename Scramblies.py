'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''

def scramble(str1, str2):
    letters_str1 = {a:str1.count(a) for a in set(str1)}
    letters_str2 = {a:str2.count(a) for a in set(str2)}
    for i in letters_str2: 
        if i not in letters_str1: return False
    for letter in letters_str2: 
        if letters_str1[letter] < letters_str2[letter]: return False
    return True
