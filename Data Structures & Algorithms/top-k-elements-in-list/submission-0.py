class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # question is saying i want a number of elements, k, from the list that are the most frequent

        # top most freq k elements --> heap
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        minHeap = []
        for num in count.keys():
            # will push sorting by count[num] as first index in the tuple
            heapq.heappush(minHeap, (count[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        # returning list
        ans = []
        for i in range(k):
            # append the num val not the freq to the ans
            ans.append(heapq.heappop(minHeap)[1])
        return ans



        # bucket sort is faster -->
        # you know the number of distinct elements in the num is greater than k
        # because of constraint can make a hashtable which is initialized as empty list with a length of nums
        # most frequent is at the end of the array
        # reverse loop order after populating enumerating nums and storing frequency