matrix = []
matrix2 = []
N = int(input())

for test in range(N):
    matrix.append(input())

for test in range(N):
    matrix2.append(input())

for i in range(8):
    for j in range(8):
        if matrix2[i][j] == 'X':
            if i == 0 or i == 7 or j == 0 or j == 7:
                