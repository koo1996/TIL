N = int(input())

cnt = 4

for i in range(N+1):

    string_ = str(i)

    for j in string_:
        if not(j == '4' or j == '7'):
            break
    else:
        cnt = int(i)

print(cnt)