# -*- coding: utf-8 -*-
import random

"""
import this
The Zen of Python, by Tim Peters
"""

def generate():
    text = []
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

    r = random.randint(1,18)
    return text[r]
