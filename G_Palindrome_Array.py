n=int(input())
l=list(map(int,input().split()))
co=0
for i in range(0,n):
    if l[i]==l[n-1-i]:
        co+=1
if co==n:
    print('YES')
else:
    print('NO')