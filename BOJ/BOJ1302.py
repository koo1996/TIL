N = int(input())
dic = {}
for i in range(N):
    a = input()
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1

list=[]

num = max(dic.values())

for j in dic:
    if num == dic[j]:
        list.append(j)
list.sort()
print(list[0])