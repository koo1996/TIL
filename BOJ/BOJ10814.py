N = int(input())
member_ = []

for i in range(N):
    age, name = map(str,input().split())
    age = int(age)
    member_.append((age,name))

member_.sort(key = lambda x : x[0])

for j in member_:
    print(j[0],j[1])