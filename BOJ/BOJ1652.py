matrix = []
N = int(input())
for test in range(N):
    M = input()
    matrix.append(M)

result1 = 0
for i in range(N):
    cnt1 = 0
    for j in range(len(M)):
        if matrix[i][j] == '.':
            cnt1 += 1
            if cnt1 == 2:
                result1 += 1
            elif cnt1 >= 3:
                break
        else:
            cnt1 = 0


result2 = 0
for j in range(len(M)):
    cnt2 = 0
    for i in range(N):
        if matrix[i][j] == '.':
            cnt2 += 1
            if cnt2 == 2:
                result2 += 1
            elif cnt2 >= 3:
                break
        else:
            cnt2 = 0
print(result1, result2)