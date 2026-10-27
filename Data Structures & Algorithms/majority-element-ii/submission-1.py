class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []

        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        for k, v in freq.items():
            if v > math.floor(len(nums)/3):
                res.append(k)

        return res
        