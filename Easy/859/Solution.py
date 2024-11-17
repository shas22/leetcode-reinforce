class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
            
        if s == goal:
            return len(set(s)) < len(s)
        
        mismatches = []
        for i, (char1, char2) in enumerate(zip(s, goal)):
            if char1 != char2:
                mismatches.append((char1, char2))

                if len(mismatches) > 2:
                    return False
                    
        return len(mismatches) == 2 and mismatches[0][0] == mismatches[1][1] and mismatches[0][1] == mismatches[1][0]
                        

