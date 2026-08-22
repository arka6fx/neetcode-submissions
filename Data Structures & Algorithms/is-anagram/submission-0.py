class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1

        for char in t:
            if char not in hashmap:
                return False
            hashmap[char] -= 1

        for val in hashmap.values():
            if val != 0:
                return False

        return True        
        