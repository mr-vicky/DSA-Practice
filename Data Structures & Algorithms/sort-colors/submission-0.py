class Solution:
    def sortColors(self, nums: List[int]) -> None:
        res = []
        for x in nums:
            if x == 0:
                res.append(x)

        for x in nums:
            if x == 1:
                res.append(x)

        for x in nums:
            if x == 2:
                res.append(x)

        for i in range(len(res)):
            nums[i] = res[i]
                