from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create key based on ascii for each word
        #make list into tuple 
        # add to a dictionary 
        # return dict values 
        words = defaultdict(list)

        for word in strs:
            #for 26 letters
            #[0][0][0] .... [0]
            # represents: a b c

            counter = [0] * 26
            for char in word:
                askey = ord(char) - ord('a')
                counter[askey] +=1
                
            words[tuple(counter)].append(word)
        return words.values()
