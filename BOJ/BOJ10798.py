matrix = []

for _ in range(5):
    matrix.append(input())

for i in range(max(len(k) for k in matrix)):
    for j in range(5):
        if i < len(matrix[j]):
            print(matrix[j][i], end="")
