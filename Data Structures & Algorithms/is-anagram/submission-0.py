class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            # return False
            return False
        from collections import Counter

        s_dic= Counter(s)
        t_dic = Counter(t)
        print(s_dic,t_dic)
        for i in s_dic.keys():
            if s_dic[i] != t_dic[i]:
                return False
        return True