N = int(input())

for test in range(1, N+1) : #N번 반복
    word = input() 
    for i in range(len(word)//2) :
        if word[i] == word[-1-i] : #자릿수 비교
            answer = 1 
        else :
            answer = 0
    print("#{} {}".format(test, answer))