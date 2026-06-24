
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mydict = defaultdict(list)


        for s in strs:

            key = ''.join(sorted(s))

            mydict[key].append(s)

        

        return list(mydict.values())