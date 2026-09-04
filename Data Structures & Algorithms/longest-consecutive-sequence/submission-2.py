class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        nums = set(nums)

        for i in nums:
            if i - 1 not in nums:
                cur = 1

                while i + 1 in nums:
                    cur += 1
                    i += 1

                longest = cur if longest < cur else longest
        return longest
