# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:16:29 2024

@author: Guy
"""
import numpy as np
 
Run = False

while Run == False:

    n = input('Number of loads: ')

    try:

        int(n)

        Run = True

    except:

        Run = False

n=int(n)
 
R_Home = float(input('Enter home load: '))

R_Line = float(input('Enter line load: '))

V = float(input('Enter input Voltage: '))
 
G = np.array(np.zeros((n,n)))
 
for i in range(n):

    for j in range(n):

        if i == j:

            G[i][j] = -((2/R_Line)+(1/R_Home))

        elif i == j+1:

            G[i][j] = (1/R_Line)

        elif i == j-1:

            G[i][j] = (1/R_Line)

        else:

            G[i][j] = 0
 
G[n-1][n-1] = -((1/R_Line)+(1/R_Home))
 
Y = np.array(np.zeros((n,1)))

Y[0][0] = -V/R_Line
 
print(np.dot(np.linalg.inv(G),Y))
 
