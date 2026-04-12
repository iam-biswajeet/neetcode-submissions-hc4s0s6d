class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-k for k in nums ]
        heapq.heapify(nums)
        while k>0:
            val=heapq.heappop(nums)
            if k==1:
                return -val
            k=k-1
        