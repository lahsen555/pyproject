


def pgcd(a,b):
    r=a%b
    if r == 0:
        return b
    else:
        return pgcd(b,r)
    
print(pgcd(21,14))