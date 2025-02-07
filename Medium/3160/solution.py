class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        user_scores = {}
        
        score_frequency = Counter()
        
        distinct_scores = []
        
        for user_id, new_score in queries:
            score_frequency[new_score] += 1
            
            if user_id in user_scores:
                old_score = user_scores[user_id]
                score_frequency[old_score] -= 1
                
                if score_frequency[old_score] == 0:
                    score_frequency.pop(old_score)
            
            user_scores[user_id] = new_score
            
            distinct_scores.append(len(score_frequency))
        
        return distinct_scores