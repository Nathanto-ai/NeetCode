from typing import List

from sympy import product


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]

        prefixProduct = 1
        for i in range(len(nums)):
            products[i] *= prefixProduct
            prefixProduct *= nums[i]

        suffixProduct = 1
        for x in range(len(nums) - 1, -1, -1):
            products[x] *= suffixProduct
            suffixProduct *= nums[x]

        return products


if __name__ == "__main__":
    temp = Solution().productExceptSelf([1, 2, 4, 6])
    print(temp)
