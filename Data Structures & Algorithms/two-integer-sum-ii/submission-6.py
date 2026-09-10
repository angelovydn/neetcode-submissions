class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # [2, 3, 5, 8, 15]
        # Target: 13
        # 1-indexed

        for i in range(len(numbers)):

            l = i+1 # index1 < index2
            r = len(numbers) - 1
            diff = target - numbers[i]
            while l <= r:
                m = l+(r-l)//2
                if numbers[m] == diff: return [i+1, m+1]
                elif numbers[m] < diff: l=m+1
                else: r=m-1
        return []