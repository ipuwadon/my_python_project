from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i, num in enumerate(nums):
            print(f"target is {target} and num is {num}")
            complement = target - num
            print(complement)

            if complement in seen:
                print(seen)
                return [seen[complement], i]
            seen[num] = i
            print(seen)


nums = [10,5,2,1,7]
target = 9

ts = Solution()
rs = ts.twoSum(nums, target)

print(rs)

print(4+6//10)