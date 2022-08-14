A = input()
B = input()

Q1 = int(A) * int(B[2])
Q2 = int(A) * int(B[1])
Q3 = int(A) * int(B[0])
print(Q1,Q2,Q3,sep='\n')
print(Q1 + Q2 * 10 + Q3 * 100)