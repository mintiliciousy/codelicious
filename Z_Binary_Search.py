N,Q=list(map(int,input().split()))
A=list(map(int,input().split()))
for i in range(Q):
    A.sort()
    flag='not found'
    X=int(input())
    low, high = 0, len(A) - 1
    while low <= high and X<=A[-1]:
        mid = (low + high) // 2
        if A[mid] == X:
            flag='found'
            break
        elif A[mid] < X:
            low = mid + 1
        else:
            high = mid - 1
    if flag=='found':
        print("found")
    else:
        print("not found")