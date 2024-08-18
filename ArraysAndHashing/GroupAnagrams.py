from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = dict()
        for string in strs:
            sortedStr = "".join(sorted(string))
            if sortedStr not in strDict:
                strDict[sortedStr] = [string]
            else:
                strDict[sortedStr].append(string)
        return list(strDict.values())


if __name__ == "__main__":
    temp = Solution().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
    print(temp)
