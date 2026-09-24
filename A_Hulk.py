n=int(input())
hate='I hate it'
hate_that='I hate that'
love='I love it'
love_that='I love that'
for i in range(1,n+1):
    if i%2==0:
        if i==n:
            print(love)
        else:
            print(love_that,end=' ')
    else:
        if i==n:
            print(hate)
        else:
            print(hate_that,end=' ')