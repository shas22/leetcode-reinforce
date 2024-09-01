#Simple hash map implementation

Class Pair:
def __init__(self, key, val):
    self.key = key
    self.val = val

Class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map=[None, None]

    def hash(self, key):
        key_count = 0 
        for c in key:
            key_count += ord(c)
        return key_count % self.capacity
    
    # Open addressing implementation
    def get(self, key):
        index = self.hash(key)
        
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None

    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            
            index += 1
            index = index % self.capacity
    
    def remove(self, key):
        if not self.get(key):
            return
        
        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                # buggy implementation as Get might not work
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)
    
    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)
"""
Hashmaps look like this:

------|---------------|
index | Key,    Value | 
    0 | "Sarah", "USA"|
    1 | "YT",    "SG" |

It is called a hashmap because the Key of the key-value pair is hashed to become an integer which becomes the index of where the k-v will be stored. 

For example, the hashing could be sum of the ASCII of each letters mod by length of the hashmap in the Key in this case it'll be 173. 

Sum of ASCII of key % len(hashmap) = index of next element

173 % 2 = 1 <- sarah goes to index 1
495 % 2 = 0 <- sarah goes to index 0

Some math behind how it always finds the right index is dependant on the length of the hashmap as the result of key%length has to be lower than the length no matter what. 


The underlying implementation of a hashmap is more complicated as it has collision resolution and more operations like bit masking, shifting and other techniques that I currently do not know to help with performance and efficient memory usage. 


Open addressing:
1. In open addressing, if there is a collision the algorithm will search for the next open spot from the modulo-ed index. If it goes out of bounds then it will increase the capacity.
"""


