class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        cnt = 0
        for x in nums:
            if x != val:
                res.append(x)
                cnt += 1
        print(res, cnt)
        for i in range(0, len(res)):
            nums[i] = res[i]
        return cnt