# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:15:32 2018

@author: Siva
"""

#Modules
if __name__=="__main__":
    print("first_module executing.")
else:
    print("first_modue is being called.")
    
def isPaliandrome(word):
    reverseWord=word[::-1]
    return word.lower()==reverseWord.lower()