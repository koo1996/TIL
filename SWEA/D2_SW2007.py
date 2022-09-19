N = int(input())

for i in range(1, N + 1):
    M = input()
    word = ''
    for j in M:
        word += j
        length = len(word)
        if word == M[length:length+length]:
            break
    print('#{} {}'.format(i, len(word)))