import heapq

heap = []

N = int(input())

for i in range(N):
    n = int(input())

    if n != 0:
        heapq.heappush(heap, n)
    else:
        if len(heap) == 0:
            print(0)
        else:    
            print(heapq.heappop(n))
