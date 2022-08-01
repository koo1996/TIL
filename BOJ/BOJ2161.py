from collections import deque

n = int(input())
queue = deque(range(1,n+1)) 

while len(queue) > 1: #길이가 1보다 작을때까지 반복
    print(queue.popleft(), end=" ") #첫번째자리의 숫자를 삭제하고 출력
    queue.append(queue.popleft()) #수정된 값에서 첫번째자리의 숫자를 삭제하고 마지막자리에 추가한다.


print(queue[0]) #삭제되고 남은 값 출력

