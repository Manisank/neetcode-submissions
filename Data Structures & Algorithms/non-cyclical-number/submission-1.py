class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n!=1 and n not in seen:
            seen.add(n)
            total = 0
            for dig in str(n):
                total += int(dig)**2
            n =total
        return n==1



