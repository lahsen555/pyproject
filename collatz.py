
import matplotlib.pyplot as plt



def gold(n):
    m=[]
    while n!=1:
        m.append(n)
        if n%2 ==0:
            n=int(n/2)
        else:
            n=int(3*n + 1)
    m.append(1)
    return m
            
            
plt.plot(gold(7),marker = "o")
plt.plot(gold(11), marker = "o")
plt.plot(gold(23), marker = "o")
plt.plot(gold(28), marker = "o")
#plt.legend("green","blue")
plt.show()