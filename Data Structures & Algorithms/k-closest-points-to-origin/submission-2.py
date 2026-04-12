class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap=[]

        for i in range(len(points)):
            val=points[i]
            dist=math.sqrt(val[0]**2 + val[1]**2)
            heapq.heappush(min_heap,[dist,val])
        
        res=[]
        print(min_heap)
        for i in range(k):
            
            res.append(heapq.heappop(min_heap)[1])
        return res



        