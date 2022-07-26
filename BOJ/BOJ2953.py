result = [] #빈 리스트 생성
for test in range(5): #5번 반복
    numbers = map(int,input().split()) #각 참가자의 점수 저장
    result.append(sum(numbers)) #점수 총합을 result리스트에 저장
print('{} {}'.format(result.index(max(result))+1,max(result))) 
#result 리스트에서 최대값과 위치(index는 0부터 시작하니까 +1 해준다.)를 출력