a,b = map(int,input().split())
list_number = list(map(int,input().split()))
for i in range(a):
    if list_number[i] < b:
        print(list_number[i],end=' ')