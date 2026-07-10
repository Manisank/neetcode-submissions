class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ''
        for dig in digits:
            digit += str(dig)
        res = int(digit)+1
        return [int(char) for char in str(res)]