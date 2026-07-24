class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:           # early exit: smallest number already > 0
                break
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate 'i'
                continue

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])

                    # move past duplicates on left and right
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res