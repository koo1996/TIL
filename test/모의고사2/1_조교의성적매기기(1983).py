T = int(input()) #테스트케이스 생성

for test in range(1,T+1):
    result = [] #각 학생들이 총점을 저장할 리스트 생성
    N,K = map(int,input().split())
    for i in range(N):
        MID, FINAL, HW = map(int,input().split()) #총점 구하기
        sum = MID * 0.35 + FINAL * 0.45 + HW * 0.2
        result.append(sum)
    result2 = [] #각 학생들이 등수를 저장할 리스트 생성
    for j in range(len(result)):
        cnt = 1
        for k in range(len(result)):
            if result[j] < result[k]: #자신보다 높은 점수를 가진 학생이 있다면 cnt 1씩 증가한다.
                cnt += 1
        result2.append(cnt) #학생들의 등수를 result2에 저장

    #총 학생 수 / 10 을 해서 학점 비율을 맞추고 해당되는 범위에 존재하는 학점을 부여한다.       
    if result2[K-1] <= (N / 10): 
        grade = 'A+'
    elif result2[K-1] <= 2 * (N / 10):
        grade = 'A0'
    elif result2[K-1] <= 3 * (N / 10):
        grade = 'A-'
    elif result2[K-1] <= 4 * (N / 10):
        grade = 'B+'
    elif result2[K-1] <= 5 * (N / 10):
        grade = 'B0'
    elif result2[K-1] <= 6 * (N / 10):
        grade = 'B-'
    elif result2[K-1] <= 7 * (N / 10):
        grade = 'C+'
    elif result2[K-1] <= 8 * (N / 10):
        grade = 'C0'
    elif result2[K-1] <= 9 * (N / 10):
        grade = 'C-'
    elif result2[K-1] <= 10 * (N / 10):
        grade = 'D0'
    print(f'#{test}',grade) #결과값 출력