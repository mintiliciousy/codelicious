n=int(input())
c,m=0,0
for i in range(n):
    a,b=map(int,input().split())
    if a>b:
        m+=1
    elif b>a:
        c+=1
    else:
        c+=1
        m+=1
if c>m:
    print("Chris")
elif m>c:
    print("Mishka")
else:
    print("Friendship is magic!^^")