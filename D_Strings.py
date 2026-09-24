A=input()
B=input()
print(len(A),len(B))
print(A+B)
A,B=B[0]+A[1:],A[0]+B[1:]
print(A,B)