
# All of Pascal's programming


# IMPORTS


import numpy as np
import math
from numpy import linalg as la
from scipy.linalg import null_space
from scipy.linalg import lu


# SEQUENCES


# Prime numbers
def primenum(n): # n is the highest number value function will check if it is a prime or not
    lst = [2]
    for i in range (3,n):
        for j in range (len(lst)):
            if i%lst[j]==0:
                break
        else:
            lst.append(i)

    lst.insert(0,1)
    return lst

# Fibonacci numbers
def fibnum(n):
    lst=[]
    a=0; c=1
    for i in range (n):
        lst.append(c)
        b=c
        c+=a
        a=b
    return lst

# Triangular numbers
def triangnum(n):
    lst = []
    for i in range (n):
        lst.append(i*(i+1)/2)
    return lst


# TRIANGLE PASCAL


def pascal(n,c, d='c'):  # Pascal function returns the Pascal's triangle with different parameter values c,d
    if d=='c':
        d = c
    a=[] # the Pascal list
    for i in range(n+1):
        a.append([]) # creating a new list in the list
        a[i].append(c) # first number (left most side of row) is c
        for j in range(1,i): # loop for row i
            a[i].append(a[i-1][j-1]+a[i-1][j]) # append the number above on left side + above on right side.
        if(n+1!=0): # to remove list being out of range for Pascal's Triangle past 0th row...
            a[i].append(d) # we add the value 'd' at the end of the triangle (right side)
#    if c == int(c) and d == int(d):
#        a=a.astype(int)
    return a

def pascalSeq(a,seq, pr=True): # prints Pascal's triangle and looking for a sequence
    lst = []
    n = len(a)
    if pr==True: # if true, then print Pascal's triangle
        for i in range(n):   # now we print all the rows
            print('   '*(n-i),end='',sep='')
            for j in range(0,i+1):
                for k in range(len(seq)):

                    if a[i][j] == seq[k]:
                        print('\\033[94m{0:6}'.format(a[i][j]),end='',sep='') # change colour to all specified numbers
                        if a[i][j]!=1:
                            lst.append(a[i][j])
                        break
                else:
                    print('\\033[0m{0:6}'.format(a[i][j]),end='',sep='') # this format will keep it looking like a triangle
            print('\\n')
    else:
        for i in range(n):   # now we print all the rows
            for j in range(0,i+1):
                for k in range(len(seq)):
                    if a[i][j] == seq[k] and a[i][j]!=1:
                        lst.append(a[i][j])
                        break
    return lst

def pascalMulti(n,c, d='c'):  # Pascal function returns the Pascal's triangle with different parameter values
    if d=='c':
        d = c
    a=[] # the Pascal list
    for i in range(n+1):
        a.append([]) # creating a new list in the list
        a[i].append(c) # first number (left most side of row) is c
        for j in range(1,i): # loop for row i
            a[i].append(a[i-1][j-1]*a[i-1][j]) # append the number above on left side + above on right side.
        if(n+1!=0): # to remove list being out of range for Pascal's Triangle past 0th row...
            a[i].append(d) # we add the value 'd' at the end of the triangle (right side)
    return a

def pascalDiv(a,num=0,pr=True):   # prints Pascal's triangle and looking for all values divisible by num
    lst = []
    n = len(a)
    if pr==True:
        for i in range(n):   # now we print all the rows
            print('   '*(n-i),end='',sep='')
            for j in range(0,i+1):
                if abs(a[i][j]) % num == 0:
                    print('\\033[94m{0:6}'.format(a[i][j]),end='',sep='') # this format will keep it looking like a triangle
                    if a[i][j]!=1:
                        lst.append(a[i][j])
                else:
                    print('\\033[0m{0:6}'.format(a[i][j]),end='',sep='') # this format will keep it looking like a triangle
            print('\\n')
    else:
        for i in range(n):   # now we print all the rows
            for j in range(0,i+1):
                if a[i][j] % num == 0 and a[i][j]!=1:
                    lst.append(a[i][j])
    return lst

def pascalSeqDiv (a, seq, num=0, r=2, pr=True): # prints Pascal's triangle and looking for a sequence
    lst = []
    lst2 = []
    n = len(a)
    if pr==True: #if true, then print Pascal's triangle
        for i in range(n):   # now we print all the rows
            print('   '*(n-i),end='',sep='')
            for j in range(0,i+1):
                for k in range(len(seq)):

                    if abs(a[i][j]) == seq[k] and abs(a[i][j]) % num == 0:
                        print('\\033[93m{0:6}'.format(round(a[i][j],r)),end='',sep='') # change colour to all specified numbers
                        if a[i][j]!=1:
                            lst.append(a[i][j])
                            lst2.append(a[i][j])
                        break
                    elif abs(a[i][j]) == seq[k]:
                        print('\\033[94m{0:6}'.format(round(a[i][j],r)),end='',sep='') # change colour to all specified numbers
                        if a[i][j]!=1:
                            lst.append(a[i][j])
                        break
                    elif abs(a[i][j]) % num == 0:
                        print('\\033[92m{0:6}'.format(round(a[i][j],r)),end='',sep='') # change colour to all specified numbers
                        if a[i][j]!=1:
                            lst2.append(a[i][j])
                        break
                else:
                    print('\\033[0m{0:6}'.format(round(a[i][j],r)),end='',sep='') # this format will keep it looking like a triangle
            print('\\n')
    else:
        for i in range(n):   # now we print all the rows
            for j in range(0,i+1):
                for k in range(len(seq)):
                    if a[i][j] == seq[k] and a[i][j]!=1:
                        lst.append(a[i][j])
                        break
    return lst, lst2


# MATRIX PASCAL


def pasmatrix(n,c,d='c'): # Prints the pascal matrix
    if d=='c': # If d is not inserted, then it will be the same value as c
        d=c
    a = np.zeros((n,n))
    for i in range (n):
        a[i][0] = c
        a[0][i] = d

    i=1; j=1
    while i<n:
        while j<n:
            a[i][j] = int(a[i][j-1]+a[i-1][j])
            a[j][i] = int(a[i][j])
            j+=1
        i+=1
        j=1
    if c == int(c) and d==int(d):
        a=a.astype(int)
    return a

def pasSeq(a,seq, pr=True): # IN A MATRIX prints Pascal's triangle and looking for a sequence
    n = len(a)
    b = np.zeros((n,n))
    if pr==True: # If true, then print Pascal's triangle
        for i in range(n):   # Now we print all the rows
            for j in range(0,i+1):
                for k in range(len(seq)):
                    if abs(round(a[i][j])) == seq[k]:
                        print('\\033[94m{0:6}'.format(a[i][j])) # Change colour to all specified numbers
                        if abs(round(a[i][j]))!=1:
                            b[i][j] = abs(round(a[i][j]))
                        break
                else:
                    print('\\033[0m{0:6}'.format(a[i][j])) # This format will keep it looking like a triangle
        return b
    else:
        lst= []
        for i in range(n):   # Now we print all the rows
            for j in range(0,i+1):
                for k in range(len(seq)):
                    if abs(round(a[i][j])) == seq[k] and a[i][j]!=1:
                        lst.append(abs(round(a[i][j])))
                        break
    return lst

def printy(a):   # Prints a big matrix pretty sometimes
    s = [[str(e) for e in row] for row in a]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\\n'.join(table))
    return

def facting(a): # Returns nxn matrix with # of prime numbers each value can be divided by
    val = 0
    n = np.size(a,1)
    b = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            m = a[i,j].astype(int)
            for k in range(1,m):
                if a[i,j]%k == 0:
                    b[i,j]+=1
    return b.astype(int)

def priming(a): # Returns nxn matrix of the greatest prime numbers
    n = np.size(a,1)
    b=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            k = 2
            m = a[i,j]
            while k * k < m:
                 while m % k == 0:
                     m = m / k
                 k = k + 1
            if a[i,j]==m:
                b[i,j]=m
            else:
                b[i,j]=0
    return b.astype(int)

def lurow(a): # Finds the 1's in each row & returns the nth column with 1 in it by order from top to bottom row.
    lst = []
    m = np.size(a,1)
    for i in range (m):
        for j in range(m):
            if a[i,j]==1:
                lst.append(j+1)
    return lst,

def lucol(a): # Finds the 1's in each column & returns the nth row with 1 in it by order from left to right column.
    lst = []
    m = np.size(a,1)
    for j in range (m):
        for i in range(m):
            if a[i,j]==1:
                lst.append(i+1)
    return lst

def onefinder(a): # Returns the location where 1s are found
    lst=[],
    m = np.size(a,1)
    for i in range (m):
        for j in range(m):
            if a[i,j]==1:
                lst.append([i,j])
    return lst

def onefiner(n): # Returns the location where 1s are found in ALL matrices with n and less than n rows
    lst=[]
    for i in range(1,n):
        b = la.inv(pasmatrix(i,1)).astype(int)
        primb = onefinder(abs(facting(b)))
        lst.append(primb)
    return lst

def pasmatrixall(n,c=1,d=1, printit=True): # Returns and prints all pascal matrices from 2x2 to nxn (total of n-1 matrices)
    for i in range(n):
        a =  pasmatrix(n-i,c,d)
        if printit == True:
            print(a)
        yield a

def pasmatrixallinv(n,c=1,d=1, printit=True): # Returns and prints all INVERSE pascal matrices from 2x2 to nxn (total of n-1 matrices)
    for i in range(n):
        a =  la.inv(pasmatrix(n-i,c,d))
        if printit == True:
            print(a)
        yield a
        
def prod(lst): # https://rosettacode.org/wiki/Determinant_and_permanent#Python
    return reduce(mul, lst, 1)
 
def perm(a): # https://rosettacode.org/wiki/Determinant_and_permanent#Python
    n = len(a)
    r = range(n)
    s = permutations(r)
    return fsum(prod(a[i][sigma[i]] for i in r) for sigma in s)

