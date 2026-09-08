class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r = 0, len(heights)-1
        _max = 0
        while l<r:
            _max = max(_max, (r-l)*min(heights[l],heights[r]))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            print((r-l)*min(heights[l],heights[r]))
        
        return _max