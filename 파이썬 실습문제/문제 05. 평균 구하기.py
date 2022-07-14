#주어진 숫자의 평균을 구하는 코드를 작성하시오.
#sum(), len()  함수 사용 금지
numbers = [3, 10, 20]
i = 0 
sum = 0 #분자(합계)
m = 0 #분모(갯수) 
for i in numbers:
    sum += i
    m += 1
print(int(sum/m))
