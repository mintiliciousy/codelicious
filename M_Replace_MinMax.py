n=int(input())
l=list(map(int,input().split()))
i=min(l)
io=l.index(i)
j=max(l)
jo=l.index(j)
l[io],l[jo]=l[jo],l[io]
print(*l)