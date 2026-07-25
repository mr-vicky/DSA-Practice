class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}

        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x]  = 1

        largest = -1

        for key in freq:
            if freq[key] == 1:
                largest = max(largest, key)
            
        return largest