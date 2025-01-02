class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        
        valid_words_index = []
        for index, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                valid_words_index.append(index)
                
        ans = []

        for left, right in queries:
            count = bisect_right(valid_words_index, right) - bisect_left(valid_words_index, left)

            ans.append(count)
            
        return ans