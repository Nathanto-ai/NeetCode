from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        solveSet = set()

        for num in nums:
            if num in solveSet:
                return True
            solveSet.add(num)

        return False


if __name__ == "__main__":
    temp = Solution().hasDuplicate([1, 2, 3, 5, 4])
    print(temp)
