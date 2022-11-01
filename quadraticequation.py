# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 21:15:15 2022

@author: nelso
Title: quadratic equation
Status: ongoing(maybe done)
"""
import numpy as np



def checkint(x):
    if x == (int)(x):
        return (int)(x)
    else:
        return x

def solvequad(a,b,c):
    #quadratic_equationp = (((-1 * b)+(np.sqrt((b**2) - (4*a*c))))/(2*a))
    #quadratic_equationm = (((-1 * b)-(np.sqrt((b**2) - (4*a*c))))/(2*a))
    
    insideroot = (b**2) - (4*a*c)
    if insideroot <0:
        print("error tis complex you fuckface")
    else:
        quadratic_equationp = (((-1 * b)+(np.sqrt((b**2) - (4*a*c))))/(2*a))
        quadratic_equationm = (((-1 * b)-(np.sqrt((b**2) - (4*a*c))))/(2*a))
        simr1 = f"(x+{-1*checkint(quadratic_equationp)})"
        simr2 = f"(x+{-1*checkint(quadratic_equationm)})"
        #print(quadratic_equationm,quadratic_equationp )
        print(simr1,simr2)


solvequad(1,6,6)