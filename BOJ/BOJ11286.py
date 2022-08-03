import sys
input = sys.stdin.readline

import heapq

n = int(input())
heap = []

for _ in range(n):
    
    i = int(input())

    if i == 0 and len(heap)!=0:       
        print(heapq.heappop(heap)[1]) 
    elif i == 0 and len(heap)==0 :    
        print(0)
    else:
         heapq.heappush(heap, (abs(i),i))