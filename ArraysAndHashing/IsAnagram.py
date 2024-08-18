class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        if len(s) == len(t):
            return True

        for i in range(0, len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)

        if sCount == tCount:
            return True
        return False


if __name__ == "__main__":
    temp = Solution().isAnagram("adfasde", "asdfeade")
    print(temp)
