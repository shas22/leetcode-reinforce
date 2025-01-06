class Solution(object):
    def minOperations(self, boxes):
        with_ball = []

        for idx, box in enumerate(boxes):
            if box == "1":
                with_ball.append(idx)

        results = []
        for idx in range(len(boxes)):
            distances_sum = 0

            for current_position in with_ball:
                distance = abs(current_position - idx)
                distances_sum += distance

            results.append(distances_sum)

        return results