N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
r=0
for l in range(N):
    if A[l]==B[r]:
        r+=1
        if r==M:
            break
if r==M:
    print("YES")
else:
    print('NO')