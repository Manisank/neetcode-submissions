class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_ = set()
        for dig in nums:
            if dig not in set_:
                set_.add(dig)
        
        # Sort because sets lose the original order
        unique_elements = sorted(list(set_))
        
        # Use [:] to modify the original list in-place
        nums[:len(unique_elements)] = unique_elements
        
        return len(set_)