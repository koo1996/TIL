A,B = map(int,input().split())

X = A.replace('6','5') + B.replace('6','5')
Y = A.replace('5','6') + B.replace('5','6')
print(X,Y)