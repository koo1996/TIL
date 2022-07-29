N = int(input())
logs = dict()
for i in range(N):
    key, value = input().split()
    logs[key] = value


list_ = []
for key in logs:
 
    if logs[key] == "enter":
        list_.append(key)


list_.sort(reverse=True)
for name in list_:
    print(name)