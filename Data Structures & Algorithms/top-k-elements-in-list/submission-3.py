class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = 0
        pairs_list = []
        nums.sort()
        current = nums[0]

        # Counting the frequency of the items, and storing into the pair
        for i in range(1, len(nums)):
            if nums[i] == current:
                count += 1
            else:
                pairs_list.append((current, count))
                current = nums[i]
                count = 1
        pairs_list.append((current, count))

        # Sorting the Pair using the Frequency in desc order
        pair_sorted = sorted(pairs_list, key=lambda item: item[1], reverse=True)

        res = []
        for x, y in islice(pair_sorted, k):
            res.append(x)

        return res