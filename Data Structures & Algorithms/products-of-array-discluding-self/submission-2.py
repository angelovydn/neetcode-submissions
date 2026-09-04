class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0

        for num in nums:
            if num:
                prod *= num
            else: 
                zero_cnt +=1 

        res = [0 for _ in range(len(nums))]
        if zero_cnt > 1: return res

        for i,c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res 