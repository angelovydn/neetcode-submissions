class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # [2, 3, 5, 8, 15]
        # Target: 13
        # 1-indexed

        for i, num in enumerate(numbers):

            diff = target - num

            # sorted list -> binary search

            l, r = i+1, len(numbers)-1

            while l <= r:
                m = l + (r-l)//2
                if numbers[m] == diff: return [i+1, m+1]
                elif numbers[m] < diff: l = m+1
                else: r = m-1
            
