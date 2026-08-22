class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            pair = target - nums[i]
            if pair in hashmap:
                return [hashmap[pair],i]
            hashmap[nums[i]] = i