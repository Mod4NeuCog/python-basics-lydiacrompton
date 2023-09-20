#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:20:14 2023

@author: lydiacrompton
"""

## EXERCISE 4: Neuron 2

def main():
    V_membrane = float(-56)
    
    spike = float(input())
    V_membrane += spike
    
    print(V_membrane)
    
if __name__=='__main__':
    main()
    
    