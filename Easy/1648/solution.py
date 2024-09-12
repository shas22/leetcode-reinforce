class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        allow_dict = {}

        for char in allowed:
            allow_dict[char] = True


        for s in words:
            is_consistent = True  
            for char in s:
                if char not in allow_dict:  
                    is_consistent = False  
                    break 

            if is_consistent: 
                counter += 1

        return counter