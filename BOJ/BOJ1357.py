A,B = input().split() 
result = int(A[::-1]) + int(B[::-1]) #A,B 뒤집은 후에 더하기
result = str(result) #정수형 에서 문자형 바꾸기
print(int(result[::-1])) #결과값 뒤집고 출력 // 정수형으로 바꿔야지 필요없는 값들이 삭제됨