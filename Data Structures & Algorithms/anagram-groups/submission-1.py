class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        myMap = {}

        for s in strs:

            myMap[str(sorted(s))] = myMap.get(str(sorted(s)), []) + [s]

        res = []
        for k in myMap:
            res.append(myMap[k])
        return res 