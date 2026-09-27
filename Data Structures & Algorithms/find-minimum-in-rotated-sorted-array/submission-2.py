class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]

        l, r = 0, len(nums)-1

        # [4, 5, 6, 1, 2]
        # if l <= r then we are in the sorted part, return s[l]
        # if m > r then m is in the unsorted section
        # if m < r then m is in the sorted section; make r = m

        while l <= r:
            m = l + (r-l)//2

            if nums[l] <= nums[r]: return nums[l]   
            
            if nums[m] > nums[r]:
                l = m+1
            else:
                r=m

        return nums[l]