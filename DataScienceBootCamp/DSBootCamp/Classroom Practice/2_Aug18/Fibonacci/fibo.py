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
    
def fib2(n):
    sum=1
    print("{0}".format(sum))
    for i in range(1,n): #1,1,2,3,5,8
        print("{0}".format(sum))
        sum+=i
        