# P: A회사 1L당 ~원
# Q: B회사 R리터 이하 요금
# R: B사 기본요금 마지노선 리터
# S: R리터 초과시 1L당 요금
# W: 한달간 사용한 수도의 양

N = int(input())
result = []
for test in range(1,N+1):
    number = list(map(int,input().split()))
    use_energy_A = number[0] * number[4]
    if number[4] > number[2]:
        use_energy_B = (number[4] - number[2]) * number[3] + number[1]
    else:
        use_energy_B = number[1]
    if use_energy_A < use_energy_B:
        result.append('#%d %d' %(test,use_energy_A))
    elif use_energy_A > use_energy_B:
        result.append('#%d %d' %(test,use_energy_B))
print(*result, sep='\n')



    



