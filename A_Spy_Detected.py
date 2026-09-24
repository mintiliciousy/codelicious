n=int(input())
for i in range(n):
    leng=int(input())
    l=list(map(int,input().split()))
    for j in l:
        if l.count(j)==1:
            print(l.index(j)+1)