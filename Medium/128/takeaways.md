<h4>Topics in this problem:</h4>
Sets and trackers

<h4>Takeaways & Big ideas:</h4>
Multi variable trackers. Keeping track of multiple sequences. Need to clarify problem with some questions.

<h4>Analysis: </h4>
I didn't do clarifying questions where I should have asked if 0 length arrays would be an issue and if there would be one single and distinct sequence or there'd be multiple sub-sequences as well. Based on the test cases initially provided [100,4,200,1,3,2] and [0,3,7,2,5,8,4,6,0,1] I had made assumptions that led me down the wrong line of thought that created a half correct answer.

Due to that my initial approach had some logical errors where I didn't keep track of whether it was a sequence or not. For reference below is my final attempt which passed about half or so of the test cases before it failed. 

I went into a deeper thought on how to solve it using a hashmap for some reason and even though i eventually came to an idea to use a set I didn't think of keeping the sequences in check for some reason. 

Failed at this test case: ```[9,1,4,7,3,-1,0,5,8,-1,6]```

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # what if we made a hashmap that looks like this after one loop
        """
        {
            100: 99,
            4: 3,
            200: 199,
            1: 0,
            3: 2,
            2: 1
        }

        1. what if we make a list if complementary pairs where n - (n+1)

        2. so itll look like 96, -196, 199, -2, 1 <- doesnt work

        3. what if we had a hash map where key is n[i] and value is the -1 of the key then you check if the -1 value is inside the hashmap key. Keep a counter that increases from 1 every sequence it finds in loop 2. 
        """
        if len(nums) == 0:
            return 0

        decrement_count = defaultdict(set)
        for num in nums:
            decrement_count[num] = num - 1
        
        sq_counter = 1
        for key, value in decrement_count.items():
            if value in decrement_count.keys():
                sq_counter += 1
        return sq_counter
```
