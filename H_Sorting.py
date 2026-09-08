n=int(input())
l=list(map(int,input().split()))
for i in range(1,n):
    for j in range(0,n-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
for i in l:
    print(i,end=" ")