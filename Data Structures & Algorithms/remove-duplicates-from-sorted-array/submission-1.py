class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_indx = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[write_indx] = nums[i]
                write_indx+=1
        return write_indx
