import time
def prime(x):
    cont=0
    start=time.time()
    for i in range(1,x+1):
        if x % i == 0:
            cont+=1
        
        
    if cont==2:
        return True
    else :
         return False
    end = round(time.time()-start ,5)
    print(end)
    
    
