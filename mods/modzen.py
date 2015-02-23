# -*- coding: utf-8 -*-
import random

"""
import this
The Zen of Python, by Tim Peters
"""

def generate():
    text = []
    result = []
    r = random.randint(0,17)

    text.append('Beautiful is better than ugly.')
    text.append('Explicit is better than implicit.')
    text.append('Simple is better than complex.')
    text.append('Complex is better than complicated.')
    text.append('Sparse is better than dense.')
    text.append('Readability counts.')
    text.append('Special cases aren\'t special enough to break the rules.')
    text.append('Although practicality beats purity.')
    text.append('Errors should never pass silently.')
    text.append('Unless explicitly silenced.')
    text.append('In the face of ambiguity, refuse the temptation to guess.')
    text.append('There should be one-- and preferably only one --obvious way to do it.')
    text.append('Although that way may not be obvious at first unless you\'re Dutch.')
    text.append('Now is better than never.')
    text.append('Although never is often better than *right* now.')
    text.append('If the implementation is hard to explain, it\'s a bad idea.')
    text.append('If the implementation is easy to explain, it may be a good idea.')
    text.append('Namespaces are one honking great idea -- let\'s do more of those!')

    if r == 6 or r == 7:
        result = [text[6], text[7]]
    elif r == 8 or r == 9:
        result = [text[8], text[9]]
    elif r == 11 or r == 12:
        result = [text[11], text[12]]
    elif r == 13 or r == 14:
        result = [text[13], text[14]]
    else:
        result.append(text[r])

    return result
