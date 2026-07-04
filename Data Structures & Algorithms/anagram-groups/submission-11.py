class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_freq = defaultdict(list)

        for word in strs:
            word_freq = [0] * 26
            for char in word: word_freq[ord(char) - ord('a')] += 1

            word_freq = tuple(word_freq)
            output_freq[word_freq].append(word)

        return list(output_freq.values())