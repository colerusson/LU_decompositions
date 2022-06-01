# -*- coding: utf-8 -*-
"""Copy of LU_decompositions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q5troLH6pDcJBoMPkpsSWP6IxP8-zLex

#**Lab 5 - LU decompositions and Gaussian elimination**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab5"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Cole"

last_name="Russon"

# Enter your Math 215 section number in between the quotation marks. 

section_number="001"  

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER! 

BYUNetID="crusson"

"""**Import NumPy**"""

import numpy as np

"""**Problem 1**"""

def augment(A,b): 
  # Put your code here. 
  new_A=np.copy(A)
  new_b=np.copy(b)
  Ab=np.column_stack((new_A,new_b))
  return Ab # Put your return value here.

"""**Problem 2**"""

def first_column_zeros(A):
  B=np.copy(A)
  # Put your code here.
  for i in range(len(B)):
    for j in range(len(B[0,:])):
      if i==0:
        B[i,j]=B[i,j]
      else:
        B[i,j]=B[i,j]-(A[0,j]*A[i,0]/A[0,0])
  return B # Put your return value here.

"""**Problem 3**"""

def row_echelon(A,b): 
  # Put your code here.
  B=augment(A,b)
  for i in range(len(B)): 
      for j in range(i+1,len(B)):
          B[j]=B[j]-(B[j,i]/B[i,i])*B[i]
  return B # Put your return value here.

"""**Problem 4**"""

def LU_decomposition(A):
  m,n=np.shape(A)
  U=np.copy(A)
  L=np.identity(len(A))
  # Put your code here.
  for j in range(n-1):
    for i in range(j+1,m):
      L[i,j]=U[i,j]/U[j,j]
      U[i,:]=U[i,:]-(L[i,j]*U[j,:])
  return L,U # We've included the return values for you, though your function needs to define them correctly.

"""**Problem 5**"""

def forward_substitution(L,b): # Accepts a lower triangular square matrix L and a vector b, solves Ly=b for y.
  # Put your code here.
  n=len(b)
  y=np.zeros(n)
  for i in range(0,n):
    y[i]=(b[i]-np.dot(y,L[i,:]))/L[i,i]
  return y # Put your return value here.

"""**Problem 6**"""

def back_substitution(U,y):    # Accepts an upper triangular square matrix U and a vector b, solves Ux=b for x.
  # Put your code here.
  n=len(y)
  x=np.zeros(n)
  for i in range(n-1,-1,-1):
    x[i]=(y[i]-np.dot(x,U[i,:]))/U[i,i]
  return x # Put your return value here.

"""**Problem 7**"""

def LU_solver(A,b): 
  # Put your code here.
  U=LU_decomposition(A)[0]
  L=LU_decomposition(A)[1]
  y=forward_substitution(U,b)
  return back_substitution(L,y) # Put your return value here.

A=np.array([[1,6],[1,9]])
b=np.array([6,6])
LU_solver(A,b)

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""