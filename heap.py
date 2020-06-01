import heapq


heap_list = []
heapq.heappush(heap_list, 0)
heapq.heappush(heap_list, 1)
heapq.heappush(heap_list, 2)
heapq.heappush(heap_list, 3)
heapq.heappush(heap_list, 5)
heapq.heappush(heap_list, 4)
heapq.heappush(heap_list, 8)
heapq.heappush(heap_list, 6)
heapq.heappush(heap_list, 7)
print(heap_list)

while heap_list:
    print(heapq.heappop(heap_list))
