for _ in range(3):
    result = []
    cnt = 1
    N = list(map(int,input()))
    for i in range(8):
        if i == 7:
            result.append(cnt)
        elif N[i] == N[i+1]:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 1
    print(max(result))