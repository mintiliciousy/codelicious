n=int(input())
c='codeforces'
for i in range(n):
    p=0
    s=input()
    for j in range(len(s)):
        if s[j]==c[j]:
            p+=1
    print(10-p)