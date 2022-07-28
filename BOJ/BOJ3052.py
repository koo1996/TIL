res_list = []
for test in range(10): #10회 반복
    N = int(input())
    result = N % 42 # 42로 나누고 나머지 구하기
    res_list.append(result) #나머지값들을 리스트에 저장
print(len(set(res_list))) #중복값을 지우고 총 갯수를 출력
