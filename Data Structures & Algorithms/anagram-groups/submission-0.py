class Solution:
    def sort(self,s: str) -> str:
        return "".join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}

        for i in range(len(strs)):
            sortedd = self.sort(strs[i]) 
            if sortedd in hashmap:
                hashmap[sortedd].append(strs[i])
            else:
                hashmap[sortedd] = [strs[i]]    
        ans = []

        for val in hashmap.values():
            ans.append(val)  
        return ans    

        