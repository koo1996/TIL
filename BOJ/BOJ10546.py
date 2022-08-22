import sys
input = sys.stdin.readline

N = int(input())
member_ = {}
for _ in range(N):
    name_ = input()
    if name_ in member_:
        member_[name_] += 1
    else:
        member_[name_] = 1
for i in range(N-1):
    Pass_ = input()
    member_[Pass_] -= 1
for j in member_:
    if member_[j] == 1:
        print(j)