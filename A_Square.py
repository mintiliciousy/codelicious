n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    if l.count(l[0])==4:
        print('YES')
    else:
        print('NO')