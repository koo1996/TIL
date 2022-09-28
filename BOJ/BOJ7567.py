N = input()
sum = 10
for i in range(len(N)-1):
    if N[i] == N[i+1]:
        sum += 5
    else:
        sum += 10
print(sum)
