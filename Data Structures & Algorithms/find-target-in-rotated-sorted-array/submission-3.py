class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        while l <= r:

            m = l + (r-l)//2
            # [3,4,5,6,1,2]
            #  l   m   # r
            print(m, nums[l:r])

            # IF SORTED: if target < nums[m] --> r = m-1
            # IF NOT SORTED: if target < nums[m] --> l = m+1
            if target == nums[m]: return m

            if nums[l] <= nums[m]:
                if nums[m] > target >= nums[l]:
                    r = m-1
                else:
                    l = m+1

            else: 
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1

        return -1



        
