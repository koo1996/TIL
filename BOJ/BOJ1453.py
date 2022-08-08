N = int(input())
list_ = list(map(int,input().split())) #앉은 자리 번호 입력
result = len(list_) - len(set(list_)) #input 길이에서 중복값을 뺀 input 길이를 빼주면 결과값이 나온다. 
print(result)