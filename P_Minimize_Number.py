n=int(input())
l=list(map(int,input().split()))
count=0
def kelp(l,k):
    global count
    for i in l:
        if i%2==0:
            k.append(i//2)
        else:
            break 
    else:
        count+=1
        return kelp(k,[])
kelp(l,[])
print(count)

