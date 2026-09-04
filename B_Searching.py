n=int(input())
l=list(map(int,input().split()))
x=int(input())
if x in l:
    print(l.index(x))
else:
    print(-1)