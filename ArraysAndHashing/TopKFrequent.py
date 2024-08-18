from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build the frequency map
        freq_map = Counter(nums)

        # Step 2: Create the bucket array
        # The bucket index represents the frequency, and each bucket contains elements with that frequency
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)

        # Step 3: Collect the top k elements
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result


if __name__ == "__main__":
    temp = Solution().topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
