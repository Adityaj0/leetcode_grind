class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mydict = {}

        visited = 1

        for num in nums:
            if num in mydict:
                return True
            
            mydict[num] = visited

        
        return False