class Solution:
    def reverseString(self, s: List[str]) -> None:
        res = []
        for i in range(len(s)-1, -1, -1):
            res.append(s[i])

        for i in range(0, len(res)):
            s[i] = res[i]
        