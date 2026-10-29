class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        res.append(nums[0])

        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                res.append(nums[i+1])
        
        for i in range(0, len(res)):
            nums[i] = res[i]

        return len(res)
