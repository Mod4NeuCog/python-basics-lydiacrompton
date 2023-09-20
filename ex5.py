#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:50:47 2023

@author: lydiacrompton
"""

##EXERCISE 5

def main():
     
     membrane_potential = 0 #initialise membrane potential
     spike_value = int(input('enter spike ')) #sys.arg uses system to receive a value; comes from import sys
     
     membrane_potential += spike_value # compute new membrne potential
         
     synapticWeight= input('enter weight value  ')
     Multiplication=spike_value * synapticWeight 
     membrane_potential2= membrane_potential + Multiplication
  
     print(membrane_potential2)
    
if __name__=='__main__':
     main()
     #the way to compute a main (only runs whats inbetween the main and the end)
     

     

    
    
    