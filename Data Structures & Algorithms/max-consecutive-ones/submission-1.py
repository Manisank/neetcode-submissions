class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_count = 0
        max_count = 0
        for i in nums:
            if i == 1:
                ones_count += 1
            else:
                if ones_count > max_count:
                    max_count = ones_count
                ones_count =0 
        return max_count if ones_count < max_count else ones_count