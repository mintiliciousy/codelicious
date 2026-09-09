A,B=map(int,input().split())
S=input()
num=0
if S[A]=='-':
    s=S.split('-')
    for i in s:
        for j in i:
            if j.isdigit():
                num+=1
if num==A+B:
    print('Yes')
else:
    print('No')
