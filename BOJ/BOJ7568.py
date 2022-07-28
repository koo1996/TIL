N = int(input())
list_ = []

for i in range(N):
    weight, height = list(map(int,input().split()))
    list_.append((weight,height))

ranks = [0] * N

for a in range(N):
    A = list_[a]
    for b in range(N):
        B = list_[b]

        if A[0] > B[0] and A[1] > B[1]:
            ranks[b] += 1

for rank in ranks:
    print(rank+1, end = " ")
