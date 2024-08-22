from collections import defaultdict
from typing import Counter


class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        maxLength = 0

        for x in numSet:
            count = 1
            if x - 1 in numSet:
                continue

            while x + count in numSet:
                count += 1

            maxLength = max(maxLength, count)

        return maxLength


if __name__ == "__main__":
    temp = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])

    print(temp)
