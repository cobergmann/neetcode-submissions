class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = i + len(s1)

        def freqCounter(s):
            freqDict = defaultdict(int)
            for c in s:
                freqDict[c] += 1
            return freqDict

        checkDict = freqCounter(s1)

        while j <= len(s2):
            if freqCounter(s2[i:j]) == checkDict:
                return True
            else:
                i += 1
                j += 1
        else:
            return False