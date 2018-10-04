n=int(input("Enter n:"))
K=0
for i in range(2,n//2+1):
    if(n%i==0):
        k=k+1
        if(k<=0):
            print("prime")
        else:
            print("not prime")
