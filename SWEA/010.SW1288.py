for test in range(1, int(input())+1): #input번 반복
    N = int(input())
    numbers = [0] * 10 #0으로 채운 리스트 생성
    i = 1
    while 0 in numbers:
        num = str(N * i) #해당되는 숫자가 있으면 numbers 리스트 +1
        for j in range(len(num)):
            numbers[int(num[j])] += 1
        i += 1
    print('#{} {}'.format(test, num))
