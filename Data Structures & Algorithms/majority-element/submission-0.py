class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        res = Counter(nums)
        major_cnt = len(nums)/2
        for key in res.keys():
            if res[key] > major_cnt:
                return key