A, B = map(int,input().split())

if A % 4 != 0:
    X1 = A // 4
    Y1 = A % 4   
else: 
    X1 = A // 4 - 1
    Y1 = 4

if B % 4 != 0:
    X2 = B // 4
    Y2 = B % 4
else: 
    X2 = B // 4 - 1
    Y2 = 4

X_axis = abs(X1 - X2)
Y_axis = abs(Y1 - Y2)
print(X_axis + Y_axis)