


def fact(x):
    fac=1
    for i in range(1,x+1):
        fac=fac*i
        
    return fac
    
def prin(y):
        z=y**2
        g=fact(y)
        if (g + y)%z ==0:
            return True
            
        else:
            return False
            
for i in range(1,100):
        if prin(i):
            print(i)
            
        