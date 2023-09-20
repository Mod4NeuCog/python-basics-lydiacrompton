#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:17:34 2023

@author: lydiacrompton
"""

#EXERCISE 4: Neuron 1

import sys

def main():
    
    membrane_potential = 0 #initialise membrane potential
    spike_value = float(sys.argv[1]) #sys.arg uses system to receive a value; comes from import sys
    
    membrane_potential += spike_value # compute new membrne potential
        
    if membrane_potential>=-65: #determine wether spike has created an effect
       print("5")
        
    else :
            print("0")
    
if __name__=='__main__':
    main()
    #the way to compute a main (only runs whats inbetween the main and the end)
    

    