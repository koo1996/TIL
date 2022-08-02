# 시간초과 방지용
import sys
input = sys.stdin.readline

# 총 교과서 수 n, 교과서 더미 수 m
n, m = map(int,input().split())

# 정렬 할 수 있는지 여부 확인용
f = True

# 한 더미마다 확인해야하므로 더미의 수만큼 반복
for i in range(m):
    # 더미의 쌓인 교과서 수
    book_stack = int(input())
    # 교과서들 리스트로 받기
    book = list(map(int,input().split()))
    
    # 모든 더미가 내림차순이라면 가능하지만
    # 한 더미라도 내림차순이 아니면 불가능
    if book != sorted(book,reverse=True):
        # 정렬 불가능 표시
        f = False
        break
    
# True 면 Yes False면 No 출력
print('Yes' if f == True else 'No')