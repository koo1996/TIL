#두 수를 Input으로 받아 합을 구하는 코드이다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.


a,b = input().split()
numbers = int(a), int(b)
print(sum(numbers))

#numbers는 리스트로 정의되어 입력값을
#int(정수)로 바꾸고 numbers에 저장한 후에
#sum(numbers)했다.