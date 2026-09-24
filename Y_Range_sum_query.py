N=list(map(int,input().split()))
Q=list(map(int,input().split()))
pre=[0]*(N[0]+1)
for i in range(0,N[0]):
    pre[i+1]=pre[i]+Q[i]
for i in range(N[-1]):
    L,R=list(map(int,input().split()))
    print(pre[R]-pre[L-1])