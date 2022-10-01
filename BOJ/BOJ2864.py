A,B = input().split()

X = int(A.replace('6','5')) + int(B.replace('6','5'))
Y = int(A.replace('5','6')) + int(B.replace('5','6'))
print(X,Y)