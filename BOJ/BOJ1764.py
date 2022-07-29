N, M = map(int,input().split())
dict_ = dict()
for i in range(N):
    p = input()
    dict_[p] = "듣도못한"

list_ = []
for i in range(M):
    p = input()
    if p in dict_:
        list_.append(p)
        
list_.sort()
print(len(list_))
for p in list_:
    print(p)
