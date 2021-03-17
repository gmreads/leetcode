class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            summand_right = target - nums[i]
            if summand_right in num_index_map:
                if num_index_map[summand_right] == i:
                    # Can not use the same index twice
                    continue
                else:
                    summand_right_index = num_index_map[summand_right]
                    summand_left_index = i
                    return [summand_left_index, summand_right_index]
            else:
                # nums[i] can not be summed with any
                # other element to result in target
                continue
        # No solution exists ?
        # return [-1, -1]
