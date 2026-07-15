class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        leader = 0
        for i in range(0, n):
            for j in range(i+1, n):
                leader = max(leader, arr[j])
            arr[i] = leader
            leader = 0
        arr[n-1] = -1
        return arr