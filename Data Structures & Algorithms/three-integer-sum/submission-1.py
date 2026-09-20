class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # you know that two sum runs o n time
        # as we iterate through the list as long --> do two sum --> lower it to n^2 from n^3

        res = []
        nums.sort()

        # two sum runs on sorted array and incrementing decrementing based on conditions

        # don't worry abt dupes because will go forward an index
        for i in range(len(nums)):
            # if first and second elem are the same avoid a dupe (order in res array does not matter)
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # find the two numbers that will add to the negative of nums[i] --> make 0
            l = i+1
            r = len(nums) - 1
            while l < r:
                # print(l,r)
                sum = nums[l] + nums[r] + nums[i]
                if sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    # avoid dupes bbby moving foward an index if the val is same as the last one
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1


        return res

        # other things to improve on:
        # how to optimize:
        # have a check is the first value is pos b/c mean the rest of nums is pos and no way to get 0
        # use enumerate --> using index and val so is useful for readability and usability
        
        # things to remember
        # indications to use other solutions (2 sum in this case) does not mean jump the gun
        # still consider edge cases
