list_ = [] #빈 리스트 생성
sum = 0 #sum 초기화
for test in range(9): #입력값 리스트에 저장
    N = int(input())
    sum += N
    list_.append(N)

for i in range(len(list_)-1): #두명의 난쟁이를 뽑는 모든 경우의 수
    for j in range(i+1,len(list_)):
        if sum - list_[i] - list_[j] == 100: #9명의 난쟁이의 키 총합에서 2명의 난쟁이의 키를 뺀다
            A_ = list_[i] #뺀 값이 100이면 A,B에 list_[i], list[j] 저장
            B_ = list_[j]

list_.remove(A_) #리스트에서 A,B 값이 있으면 삭제
list_.remove(B_)
list_.sort(reverse=False) #오름차순 정렬
print(*list_, sep='\n') #결과값 출력
