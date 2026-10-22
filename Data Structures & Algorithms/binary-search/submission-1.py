class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        # need the <= because no precheck for length
        # check in the case of single element arrays --> run through and check still whether the only element is the target
        while l <= r:
            mid = (l + r) // 2
            currentVal = nums[mid]
            if currentVal == target:
                return mid
            elif currentVal > target:
                r = mid - 1
            else:
                l = mid + 1

        
        return -1