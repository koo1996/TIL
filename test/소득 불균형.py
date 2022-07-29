for i in range(1,int(input())+1):
    N = int(input())
    cnt = 0
    number = list(map(int,input().split()))
    average = sum(number) / N #리스트의 정수들 합치고 N값으로 나누기(평균)
    for j in range(len(number)):
        if number[j] <= average: # 평균값보다 작거나 같으면 cnt 1씩 증가
            cnt +=1
    print('#{} {}'.format(i,cnt)) #결과값 출력
    