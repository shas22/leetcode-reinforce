class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # chemistry = i * i+1
        # sum is team[chem] + team[chem]
        # sum of total score / possible teams = team skill strength
        # possible teams = skill length % 2
        # if [total score % possible teams] != 0 then it's return -1 

        #if possible, find the team skill strength
        

        # not possible case
        totalScore = sum(skill)
        possibleTeams = len(skill) // 2

        if totalScore % possibleTeams != 0:
            return -1
        
        ss = totalScore // possibleTeams

        count = 0
        seen = {}
        for i in range(len(skill)):
            current = skill[i]
            complement = ss - current

            if complement in seen:
                count += current * complement
                seen[complement] -= 1
                if seen[complement] == 0:
                    del seen[complement]
            else:
                seen[current] = seen.get(current, 0) + 1

        if seen:
            return -1

        return count
