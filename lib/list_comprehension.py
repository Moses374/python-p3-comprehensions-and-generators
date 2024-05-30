#!/usr/bin/env python3

def return_evens(num_list):
    if not num_list:
        return []
    elif num_list[0] % 2 == 0:
        return [num_list[0]] + return_evens(num_list[1:])
    else:
        return return_evens(num_list[1:])

    pass

def make_exclamation(sentence_list):
    if not sentence_list:
        return []
    else:
        
        return [sentence + "!" for sentence in sentence_list]

    pass