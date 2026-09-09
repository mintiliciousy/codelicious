n=int(input())
l=list(map(int,input().split()))
i=min(l)
io=l.count(i)
if io%2!=0:
    print('Lucky')
else:
    print('Unlucky')