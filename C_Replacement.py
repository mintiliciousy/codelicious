n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    if i>0:
        li.append(1)
    elif i<0:
        li.append(2)
    else:
        li.append(0)
print(*li)
