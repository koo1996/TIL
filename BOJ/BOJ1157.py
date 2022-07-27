N = input().lower() #소문자로 받기
N_list = list(set(N))
result = []
for test_1 in N_list:
    count = N.count(test_1) #test_1이 N에 몇개가 있는지 count
    result.append(count) #중복되는 갯수를 result리스트에 저장

if result.count(max(result)) >= 2: # result리스트에 최대값이 2개 이상 존재하면 ?출력
    print('?')
else:
    print(N_list[(result.index(max(result)))].upper()) 
#result리스트에서 최대값의 인덱스를 중복값 제거한 리스트(N_list)에 대입

 