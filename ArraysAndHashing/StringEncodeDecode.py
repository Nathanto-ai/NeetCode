from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decodedStrs.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decodedStrs


if __name__ == "__main__":
    temp = Solution().encode(["neet", "code", "love", "you"])
    print(temp)
    temp1 = Solution().decode(temp)
    print(temp1)
