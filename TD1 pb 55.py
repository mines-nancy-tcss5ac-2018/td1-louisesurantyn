def reverse(n):     ## renvoie l'inverse de n
    N=str(n)
    M=''
    for i in range(len(N)):
        M += str(N[len(N)-i-1])
    return(int(M))

def palindrome(n):      ## renvoie False si n n'est pas palindrome, True si il l'est
    if n==reverse(n):
        return(True)
    else:
        return(False)

def Lychrel(n):     ## renvoie True si n est Lychrel, False sinon
    i=0
    while i<51:
        i +=1
        n += reverse(n)
        if palindrome(n):
            return(False)
    return(True)


def solve(p):
    compteur = 0
    for n in range(p):
        if Lychrel(n):
            compteur += 1
    return(compteur)

assert(palindrome(7337))
#assert(Lychrel(349)==False)
assert(Lychrel(4994))

p=10000
print(solve(p))
