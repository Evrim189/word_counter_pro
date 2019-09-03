# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:41:33 2019

@author: Evrim
"""


#open file
file=open("text_file.txt")

file=file.read()


#removePunctuation: Delete punctuation mark
def removePunctuation(text):
    clean_text=""
    str_punctuation=".:,ï»()!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~¿â€˜"
    for letter in text:
           if letter not in str_punctuation:
            clean_text+=letter
    return clean_text

x=removePunctuation(file)
x=x.split()
wordcount={}
for word in x:           

    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for key in wordcount.keys():
  print ("%s %s %s %s" %(key ,'[', wordcount[key], ']'))     


        
 #for x, y in thisdict.items():
 # print(x, y) --Sonuçları yazdırırken kullan.
# case_list = {}
#for entry in entries_list:
#    if key in case_list:
#        case_list[key1].append(value)
#    else:
#        case_list[key1] = [value]