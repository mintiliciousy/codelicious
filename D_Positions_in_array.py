n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i<=10:
        print('A[' + str(l.index(i)) + '] = ' + str(i))
     
