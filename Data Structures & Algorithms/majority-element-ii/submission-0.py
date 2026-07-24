class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freq = {}
        n = len(nums)

        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        for key in freq.keys():
            if freq[key] > math.floor(n/3):
                res.append(key)

        return res
