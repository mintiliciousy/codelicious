N=int(input())
for i in range(N):
    l=int(input())
    s=input()
    s1=list(s)
    s2=[]
    for i in range(0,l+1):
        s2.append(s1[i])
        s1.remove(s1[i])
    s1.sort()
    s2.sort()
    print(s1,s2)
    if s1==s2:
        print('YES')
    else:
        print('NO')