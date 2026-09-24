s=input()
s=s.split()
for i in s:
    if i==s[-1]:
        print(i[::-1])
    else:
        print(i[::-1],end=" ")