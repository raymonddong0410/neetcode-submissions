class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        sorted array --> indicator
        return indices pair
        '''
        l = 0
        r = len(numbers) - 1

        while l < r:
            # because sorted and increasing --> if sum is larger than target --> move right pointer
            # this is because if you move the left pointer then the target will only get larger
            # logic for left pointer is flipped

            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1,r + 1]
            if sum > target:
                r -= 1
            if sum < target:
                l += 1
