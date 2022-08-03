N = int(input())
list = []
for i in range(N):
    M = int(input())
    list.append(M) #list에 저장
list_ = sorted(list) #리스트를 (오름차순)정렬한다.
print(*list_,sep='\n') #결과값을 출력