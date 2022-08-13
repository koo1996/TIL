N = int(input()) #테스트 케이스 설정

for test in range(1,N+1):
    N = set(input()) #중복된 문자를 삭제한다.
    if len(N) == 2: #길이가 2이면 Yes 아니면  No
        print(f'#{test} Yes')
    else:
        print(f'#{test} No')
