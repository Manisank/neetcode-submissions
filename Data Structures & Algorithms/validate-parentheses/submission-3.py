class Solution:
    def isValid(self, s: str) -> bool:
        brace_dic = {'(':')', '[':']', '{':'}'}
        stack = []
        for brace in s:
            if brace == '(' or brace == '{' or brace == '[':
                stack.append(brace)

            elif len(stack)>0 and brace_dic[stack[-1]] == brace :
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False

        