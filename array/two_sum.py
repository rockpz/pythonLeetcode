"""
https://leetcode-cn.com/problems/two-sum
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    another_num_to_num_index = {}
    for i, num in enumerate(nums):
        if num in another_num_to_num_index:
            return [another_num_to_num_index[num], i]
        another_num = target - num
        another_num_to_num_index[another_num] = i
    return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
