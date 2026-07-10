class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        len_ = len(numbers)

        for i in range(len(numbers)):
            j = i+1
            while j < len_:
                if numbers[i] + numbers[j] == target:
                   return[i+1,j+1]
                if numbers[i] + numbers[j] > target:
                    len_ = j
                j +=1      

