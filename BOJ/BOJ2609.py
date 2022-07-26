a,b = map(int,input().split())
max_ = 0
for test in range(1,min(a,b)+1): #a,b 둘 중에 작은 정수만큼 반복
    if a % test == 0 and b % test == 0: #a,b에 1부터 min(a,b)의 정수들을 나누고 나머지가 0인 정수들을 찾는다. 
        max_ = test   # 나머지가 0인 정수들을 result[] 하나씩 추가하고 최대값을 출력한다. (최대공약수)

min_ = a*b//max_
#result_2 = (max(a,b) / max(result)) * min(a,b)  # 최소공배수는 (a / 최대공약수) * (b / 최대공약수) * 최대공약수
print(max_,min_)