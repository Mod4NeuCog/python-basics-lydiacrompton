#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:07:28 2023

@author: lydiacrompton
"""

##EXERCISE 3:


def main():
    
    membrane_potential = 0 #initialise membrane potential
    spike_value = float(input('enter spike value  ')) #receive a spike value
    
    membrane_potential += spike_value # compute new membrane potential
        

print(membrane_potential)

if __name__=='__main__':
    main()
    #the way to compute a main (only runs whats inbetween the main and the end)
    