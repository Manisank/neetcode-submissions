class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counts_ = Counter(nums)
        for key in counts_.keys():
            if counts_[key] > (len(nums)/2):
                return key