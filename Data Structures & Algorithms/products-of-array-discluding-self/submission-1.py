class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        total = 1
        zeros = 0
        for i in nums:
            if i != 0: total *= i
            else: zeros +=1 
        
        if zeros == 0:
            for i in range(len(nums)):
                res[i] = int(total / nums[i])
            return res
        
        elif zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0: res[i] = total
            return res
        
        else: return res