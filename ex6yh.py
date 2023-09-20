#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:40:43 2023

@author: lydiacrompton
"""

#EXERCISE 6
import sys

def main():
    print ('pick your method')
    method_choice = int(input('1 or 2'))
    Simulate(method_choice)


def Simulate(method_choice):
    if method_choice == 1:
        ##write your method 1 here
        membranep = -70
        spike = int(input('enter a spike value: '))
        membranep += spike
        print (membranep, 'method 1')
        
    elif method_choice == 2:
        ## write your method 2 here
        membranepotential=-60
        spikevalue=int(input('enter a spike value'))
        membranepotential += spikevalue
        for membranepotential < -60:
            
            print(membranepotential,'method 2')
            
    
    else:
        print('error')
    
if __name__=='__main__':
    main()
    