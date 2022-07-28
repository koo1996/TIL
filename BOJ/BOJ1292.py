a,b = map(int,input().split())

result = []
for i in range(1,60):
    for j in range(i): #i를 i만큼 만들고 리스트에 저장
        result.append(i)
print(sum(result[a-1:b])) #리스트는 0부터 시작하니 a값에 -1 해준다.
