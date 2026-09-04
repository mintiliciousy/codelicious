n=int(input())
l=list(map(int,input().split()))
m=min(l)
print(m,l.index(m)+1)