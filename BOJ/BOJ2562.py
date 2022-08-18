result = []
for _ in range(9):
    N = int(input())
    result.append(N)

Max_ = max(result) 
print(Max_)
print(result.index(Max_)+1)
