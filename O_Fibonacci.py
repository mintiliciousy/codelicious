n=int(input())
l=[]
for i in range(n):
    a,b=0,1
    for j in range(i):
        a,b=b,a+b
    l.append(a)
print(l[-1])