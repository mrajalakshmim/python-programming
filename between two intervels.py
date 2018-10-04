lower=int(input("Enter the Lower Limit for the range:"))
upper=int(input("Enter the upper Limit for the range:"))
for i in range(Lower,upper+1):
    if(i%2!=0):
        print(i)
