class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''
        for word in s.lower():
            if word.isalpha() or word.isnumeric():
                clean_str += word
                # print(word)
        return (clean_str == clean_str[::-1])