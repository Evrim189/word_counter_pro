# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:58:42 2019

@author: Evrim
"""

filedeneme=open("text_file.txt")

filedeneme=filedeneme.read()

import string
def delCharacter(file):
    clear_file=""
    for symbol in file:
        if symbol not in string.punctuation:
          clear_file+=symbol
          return clear_file

print (delCharacter(filedeneme))

def removePunctuation(x):
    deneme=""
    for letter in x:
        if letter not in string.punctuation:
            deneme+=letter

print (removePunctuation(deneme))