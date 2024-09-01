class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.createMap(s) == self.createMap(t)
    
    def createMap(self, string: str) -> list:
        letter = {}
        for char in string:
            letter[char] = letters.get(char, 0) + 1
        return letter


"""
242. Valid Anagram
Solved
Easy
Topics
Companies

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

"""
