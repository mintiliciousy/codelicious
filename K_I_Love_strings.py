n=int(input())
for i in range(n):
    a,b=map(str,input().split())
    new=''
    for i,j in zip(a,b):
        new+=i+j
    if len(a)>len(b):
        new+=a[len(b)::]
    if len(b)>len(a):
        new+=b[len(a)::]
    print(new)