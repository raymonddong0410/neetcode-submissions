class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute would be a nested loop
        # res = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     res.append(product)
        # return res

        # better idea is prefix sum?
        # calc before and after the val
        # take the before multiply and so you know at that index the before will equal to 

        # would have to find the array before and after
        length = len(nums)
        pre = [0] * length
        post = [0] * length
        res = []

        pre[0] = 1
        post[length - 1] = 1

        for i in range(1,length):
            # can't get pre starting from index one cause no index before
            # nums --> 1, 2, 3....
            # pre --> 1, 1, 2....
            # pre is delayed because we want to store val of prod of prev val at that index
            pre[i] = nums[i - 1] * pre[i - 1]
        
        for i in range(length-2,-1,-1):
            post[i] = nums[i + 1] * post[i + 1]
        
        # for the result we want to multiple pre and post at that point
        # 0 accounted for --> we multiply by first and last vals in list
        for i in range(length):
            # can also make this faster by pre populating res. replacing val is constant like append is amortoried o 1
            res.append(pre[i] * post[i])
        
        return res

        # can also do prefix sum in place. same idea but use one res array
        # res = []
        
