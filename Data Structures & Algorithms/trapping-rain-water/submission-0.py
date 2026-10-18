class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Need a way to calc all the spaces between two walls --> greater than 0
        Rules:
        - left wall and right wall greater than walls in between
        - if between two walls there are wall greater than height 0 subtract that height
        
        --> Brute force? Iterate through each wall and find the the next wall it can form a container with?
        --> Honestly brute force seems weird, a shift from container w most water --> think single column
            --> not a pattern with length and height but instead how much can sit on top of this block?

        --> intuitively thinking of two pointer
            --> left stationary and shift right pointer over
            --> conditions:
                - when moving right if height is shorter track potential water --> height diff
                - if hit wall where width is > 1 and is taller than left add potential water
                - move left pointer
                - if the right wall is shorter, subtract that diff in height * width

        --> logic is flawed, what if there is a false u shape --> [4,1,3,1,5], would miscalc and return smaller
            - so now what? go back to thinking single column. calc potential water based on lower height to the left or right
            - get this by comparing the left and right




        --> stack solution --> logic need to remember the previous vals until match condition and resolves then after
            - calc height sitting on top between two walls layer by layer. 
            - potential bum resolves by subtracting all possible water up to that level (accounted for above)
        --> prefix sum --> same logic, potential water based on height to left, height on right, and how tall the wall is
        '''

        # two pointer solution

        l,r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        res = 0

        while l < r:
            # the diff in height and also the smaller max will be the water stored at that point
            # no water stored at the time we are moving the pointer
            # but only move max pointer when the smaller max becomes the larger
            if lMax < rMax:
                # use l and r pointers to track how much water at a point
                # if lMax is smaller I want to track how much water at a point being stored and move forward
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]

        return res
