import collections
import heapq

heap_array = ["A", "A", "A", "B", "B", "B", "A"]


def lastStoneWeight(A):
    heapq._heapify_max(A)
    for i in range(len(A) - 1):
        x, y = heapq._heappop_max(A), heapq._heappop_max(A)
        heapq.heappush(A, x - y)
        heapq._heapify_max(A)
    return A[0]


def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    n += 1
    ans = 0
    d = collections.Counter(tasks)
    heap = [-c for c in d.values()]
    heapq.heapify(heap)
    while heap:
        stack = []
        cnt = 0
        for _ in range(n):
            if heap:
                c = heapq.heappop(heap)
                cnt += 1
                if c < -1:
                    stack.append(c + 1)
        for item in stack:
            heapq.heappush(heap, item)
        ans += heap and n or cnt  # == if heap then n else cnt
    return ans


leastInterval(["A", "A", "A", "B", "B", "B", "B"], n=2)
