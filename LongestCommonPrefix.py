class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        sortedstrs = sorted(strs)

        first = sortedstrs[0]
        last = sortedstrs[-1]


        count = 0

        i =0

        while i < len(first) and first[i] == last[i]:
            i+=1
            count +=1

        
        return first[:count]
            