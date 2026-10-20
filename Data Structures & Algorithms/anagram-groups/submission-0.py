class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = dict()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in ana_dict:
                ana_dict[sorted_word].append(word)
            else:
                ana_dict[sorted_word] = [word]
        return [word for word in ana_dict.values()]