class Solution:
    def sortColors(self, nums: List[int]) -> None:
        res = []
       
        for x in nums:
            if x == 0:
                res.append(0)

        for x in nums:
            if x == 1:
                res.append(1)

        for x in nums:
            if x == 2:
                res.append(2)
      
        for i in range(0, len(res)):
            nums[i] = res[i]

        

        