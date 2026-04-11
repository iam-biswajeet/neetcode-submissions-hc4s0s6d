class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.li=nums
        self.idx=k

        

    def add(self, val: int) -> int:
        self.li.append(val)
        self.li.sort()
        print(self.li)

        return self.li[len(self.li)-self.idx]

        
