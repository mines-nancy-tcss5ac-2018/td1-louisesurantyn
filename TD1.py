## Problem 16

def digitsum(n,p):
    valeur=n**p
    digits=str(valeur)
    sum=0
    for i in range(len(digits)):
        sum +=int(digits[i])
    return(sum)

def solve16(p):
    return(digitsum(2,p))



##assert solve16(15)==26
##print(solve16(1000))




## Problem 22

f = open('p022_names.txt','r')

def tri_alpha(file):
    L=[]
    for s in file:
        L=file.split(',')

def alpha_value(mot):
    value=0
    for i in range(len(mot)):
        value +=ord(mot[i])-ord('a')+1
    return(value)