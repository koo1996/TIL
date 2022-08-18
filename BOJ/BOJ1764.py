N, M = map(int,input().split())
dict_ = {}
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

# N, M = map(int,input().split())
# dict_ = {}
# for i in range(N):
#     p = input()
#     if p not in dict_:
#         dict_[p] = 1
#     else:
#         dict_[p] += 1

# for j in range(M):
#     Q = input()
#     if Q not in dict_:
#         dict_[Q] = 1
#     else:
#         dict_[Q] += 1
# list = []
# for k in dict_:
#     if dict_[k] == 2:
#         list.append(k)
# list.sort()
# print(len(list))
# print(*list,sep='\n')
