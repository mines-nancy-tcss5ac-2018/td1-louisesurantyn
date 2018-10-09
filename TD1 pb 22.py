def tri_alpha(file):
    L=file.split(',')
    L.sort()
    return(L)
    

def alpha_value(mot):
    value=0
    for i in range(1,len(mot)-1):
        value += (ord(mot[i])-ord('A')+1)
    return (value)



def solve(file):
    names = tri_alpha(file.read())
    total_name_score = 0
    for i in range(len(names)):
        total_name_score += alpha_value(names[i]) * (i+1)
    return (total_name_score)


file = open('names.txt','r')
assert(alpha_value('"COLIN"')==53)
print(solve(file))
