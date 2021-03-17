class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {nums[i]: i for i in range(len(nums))}
        for i, num in enumerate(nums):
            summand_right = target - num
            if summand_right in num_index_map and num_index_map[summand_right] != i:
                return [i, num_index_map[summand_right]]
        # No solution exists ?
        # return [-1, -1]
