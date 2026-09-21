class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        ideas: rectangle --> l * w
        - l = min of two heights
        - w = idx subtarcted from two point

        want to go through potential bigger rectangles
        --> taller it can be the better, if both heights smaller and width as well, ofc smaller
            --> if we did this would be o n^2 time 
            --> brute force
        --> height taller --> potentially can have larger area
        --> move inwards to the middle of the array to test heights

        --------> likely two pointers
        '''

        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l < r:
            # used to avoid additional calculations on shorter containers
            left_height = heights[l]
            right_height = heights[r]
            
            width = r - l
            currentArea = min(left_height, right_height) * width
            maxArea = max(maxArea, currentArea)

            if left_height < right_height:
                # increment one time at least --> avoid the infitine loop (no indices are indexed)
                l += 1
                # use less than or equal to --> avoid condition where they are equal --> not a taller container
                while l < r and heights[l] <= left_height:
                    l += 1
            # cover the opposite case and when left_height == right_height
            else:
                r -= 1
                while l < r and heights[r] <= right_height:
                    r -= 1

        return maxArea