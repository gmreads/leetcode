"""
License: Gpl v3

leetcode-link: https://leetcode.com/problems/reverse-integer/ 
"""


class Solution:
    INT_32_MAX = 2147483647
    INT_32_MIN = -2147483648

    def reverse(self, num: int) -> int:
        if num >= -9 and num <= 9:
            return num
        num_digits = self.get_number_of_digits(num)
        reversed_num = 0
        original_num = num
        num = abs(num)
        while num_digits > 0:
            curr_last_digit = num % 10
            reversed_num += curr_last_digit * (10 ** (num_digits - 1))
            num = num // 10
            num_digits -= 1
        reversed_num = -1 * reversed_num if original_num < 0 else reversed_num
        if reversed_num < INT_32_MIN or reversed_num > INT_32_MAX:
            return 0
        return reversed_num

    def get_number_of_digits(self, num: int) -> int:
        count = 0
        num = abs(num)
        while num > 0:
            num = num // 10
            count += 1
        return count
