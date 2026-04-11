class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]#max heap
        heapq.heapify(stones)
        print(stones)
        while len(stones)>1:
            largest=-heapq.heappop(stones)
            second=-heapq.heappop(stones)
            heapq.heappush(stones,- abs(largest - second))
        return -stones[0]
        