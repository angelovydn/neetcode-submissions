class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = defaultdict(int)

        for num in nums:   
            cnt[num] = cnt[num]+1
        
        cntList = [[] for i in range(len(nums) + 1)]

        for num in cnt:
            cntList[cnt[num]].append(num)
        
        cntList = cntList[::-1]

        res = []

        for entry in cntList:
            for num in entry:
                if k==0: return res
                res.append(num)
                k-=1
        return res 