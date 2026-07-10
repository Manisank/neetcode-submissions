class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        set_ = set()
        counts_ = Counter(nums)
        for key in counts_.keys():
            if counts_[key] > (len(nums)/3):
                set_.add(key)
        return list(set_)