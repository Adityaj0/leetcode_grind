class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        sortednums = sorted(nums)

        mid = len(sortednums) // 2

        return sortednums[mid]