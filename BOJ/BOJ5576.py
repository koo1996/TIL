W_TEAM = []
K_TEAM = []
W_score = 0
K_score = 0
for i in range(10):
    W_TEAM.append(int(input()))

W_TEAM.sort(reverse=True)
for x in range(3):
    W_score += W_TEAM[x]

for j in range(10):
    K_TEAM.append(int(input()))


K_TEAM.sort(reverse=True)
for x in range(3):
    K_score += K_TEAM[x]

print(W_score, K_score)