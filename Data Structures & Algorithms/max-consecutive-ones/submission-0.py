class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_count = 0
        max_count = 0
        for i in nums:
            if i == 1:
                ones_count += 1
                max_count = max(max_count, ones_count)
            else:
                ones_count = 0
        return max_count