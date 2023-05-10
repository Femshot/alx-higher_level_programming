#!/usr/bin/python3
def remove_char_at(str, n):
    '''creates a copy of the string,

    removing the character at the position n
    '''
    new_str = ''
    for i in range(0, (len(str))):
        if i != n:
            new_str += str[i]
    return new_str
