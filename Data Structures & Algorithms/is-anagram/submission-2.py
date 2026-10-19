class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq, t_freq = dict(), dict()
        if len(s) == len(t):
            for i in range(len(s)):
                s_freq[s[i]] = s_freq.get(s[i], 0) + 1
                t_freq[t[i]] = t_freq.get(t[i], 0) + 1
            else:
                return s_freq == t_freq
        else:
            return False