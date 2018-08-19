# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:38:52 2018

@author: Siva
"""

class PiggyBank:
    account_balance=0
    __init__(self):
        pass
    def startOperations(self):
        while(True):
            nextTask=input("Start (E) Or End (E):")
            if(nextTask.upper()=="END" or nextTask.upper()=="E"):
                break
            else:
                operation=input("Add (A), Withdraw (W) or Check (C):")
                if(operation.upper()=="ADD" or operation.upper()=="A"):
                    amount=input("Add amount:")
                    self.account_balance+=amount
                    
    def printBalance(self, operation):
        print()
            