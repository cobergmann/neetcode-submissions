class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(list(s))
        t_list = sorted(list(t))
        if len(s) == len(t):
            for i in range(len(s)):
                if s_list[i] != t_list[i]:
                    return False
            else:
                return True
        else:
            return False