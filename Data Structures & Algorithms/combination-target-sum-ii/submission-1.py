class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]
        nums.sort()
        def dfs(i,cur,sum):
            if sum==target:
                res.append(cur.copy())
                return
            if sum>target or i>=len(nums):
                return
            cur.append(nums[i])
            dfs(i+1,cur,sum+nums[i])
            cur.pop()
            while i+1 <len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,cur,sum)
        dfs(0,[],0)
        return res
            


        



        