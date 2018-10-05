def digitsum(n,p):
    valeur=n**p
    digits=str(valeur)
    sum=0
    for i in range(len(digits)):
        sum +=int(digits[i])
    return(sum)

def solve(p):
    return(digitsum(2,p))



assert solve(15)==26
print(solve(1000))