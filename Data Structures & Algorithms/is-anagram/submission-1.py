class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for i in s:
            if i not in s_freq:
                s_freq[i] = 0
            else: s_freq[i] += 1

        for i in t:
            if i not in t_freq:
                t_freq[i] = 0
            else: t_freq[i] += 1

        return True if s_freq == t_freq else False 
            