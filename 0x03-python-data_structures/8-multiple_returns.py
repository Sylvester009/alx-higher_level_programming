#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_len = ()
   if not sentence:
        tuple_len = 0, "None"
    else:
        tuple_len = len(sentence), sentence[0]
    return tuple_len
