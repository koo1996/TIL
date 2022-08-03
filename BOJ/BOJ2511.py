A = list(map(int,input().split()))
B = list(map(int,input().split()))
score_A = 0
score_B = 0
for i in range(len(A)):
    if A[i] < B[i]:
        score_B += 3
    elif A[i] > B[i]:
        score_A += 3
    else:
        score_A += 1
        score_B += 1
print(score_A,score_B)
if score_A > score_B:
    print('A')
elif score_A < score_B:
    print('B')
else:
    print('D')
