class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            return False


        # using ascii
        s1_counter = [0] * 26
        s2_counter = [0] * 26

        for i in range(l1):
            s1_counter[ord(s1[i]) - 97] += 1
            s2_counter[ord(s2[i]) - 97] += 1

        if s1_counter == s2_counter:
            return True

        for i in range(l1, l2):
            s2_counter[ord(s2[i]) - 97] += 1
            s2_counter[ord(s2[i - l1]) - ord("a")] -= 1
            if s1_counter == s2_counter:
                return True

        return False