# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:27:58 2024

@author: Cam Eldridge
"""
import numpy as np

#Retrive Input Data
numNodes= int(input("How many unknown voltages are there?\n"))
rLine= float(input("What is the line resistance?\n"))
rHome= float(input("What is the home resistance?\n"))
voltage= float(input("What is the source voltage?\n"))

#Build 6x6 matrix
mat= np.matrix(np.zeros((numNodes, numNodes)))

for i in range(numNodes):                       
    for j in range(numNodes):
        if i==j:
            mat[i,j]= -1*((2/rLine)+1/rHome)            #Fill diaganols
        elif abs(i-j)==1:
            mat[i,j]=(1/rLine)                          #Fill off diagonals
            
mat[numNodes-1, numNodes-1]=-1*((1/rLine)+(1/rHome))    #Fill bottom right


#Build 6x1 matrix to multiply with
rMatrix= np.matrix(np.zeros((numNodes, 1)))             
rMatrix[0, 0]= (-1*voltage/rLine)

#Invert 6x6 and dot with 6x1 to find solutions
invMat=np.linalg.inv(mat)
solution= np.dot(invMat, rMatrix)

#Print solution
print(np.matrix(solution))