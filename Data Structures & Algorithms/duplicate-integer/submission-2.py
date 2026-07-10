class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # #brute_force
        # for i in range(len(nums)):
        #     count_i = 1
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums [j]:
        #             count_i +=1
        #         if count_i >1:
        #             return True
        # return False
        # dic_ = {}
        # for i in nums:
        #     dic_[i] = nums.count(i)
        # for i in dic_.values():
        #     if i > 1:
        #         return True
        # return False

        set_ = set()
        for i in nums:
            if i in set_:
                return True
            set_.add(i)
        return False
            


        