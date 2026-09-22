class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        so we know that if the vals continue to decrease then no profit
        --> if there is a price decrease then increase, profit
        --> keep track of this profit
        --> max profit is biggest diff

        --> two pointer still kind of
        --> move left until meet smallest number

        --> another pointer move to right until next val is smaller
        --> get max profit

        --> if we have value that is smaller but not smaller than min val --> keep min val
        --> if larger profit in the future then calculate and use that 
            --> this logic requires then to check every elem larger than the min to get max profit
            --> will potentially skip past the end of the array if checking val is larger than max from before
        '''

        # starting r at 1 because need to slide r over until we hit end of list
        # not starting at end --> not sorted, also doesn't make sense for a pass
        l,r = 0,1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                # set l = r, allow to find smaller number (prices[l] < prices[r] makes sure prices[l] is a min)
                l = r
            r += 1

        return maxProfit