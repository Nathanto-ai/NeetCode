from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solveDict = {}
        for key, num in enumerate(nums):
            temp = target - num

            if num in solveDict:
                return [solveDict[num], key]
            solveDict[temp] = key

        return []


if __name__ == "__main__":
    temp = Solution().twoSum([3, 4, 5, 6], 7)
    print(temp)
