import real


n=int(input("enter an integer > 1 : "))
for i in range(n+1,2*n+1):
    if real.prime(i):
        print(i)
        