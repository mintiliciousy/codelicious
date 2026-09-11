N=list(map(int,input().split()))
Q=list(map(int,input().split()))
for i in range(N[-1]):
    L,R=list(map(int,input().split()))
    print(sum(Q[L-1:R]))