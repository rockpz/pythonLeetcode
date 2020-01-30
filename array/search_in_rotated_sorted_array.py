"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

"""

import math
from typing import List


def search(nums: List[int], target: int) -> int:
    return sub_search(nums, 0, len(nums) - 1, target)


def sub_search(nums: List[int], left_index: int, right_index: int, target: int) -> int:
    if left_index > right_index:
        return -1
    if left_index == right_index:
        if nums[left_index] == target:
            return left_index
        else:
            return -1
    if nums[right_index] > nums[left_index]:
        if nums[left_index] > target or nums[right_index] < target:
            return -1
    else:
        if (nums[right_index] < target) and (nums[left_index] > target):
            return -1
    middle_index = math.floor((left_index + right_index) / 2)
    if nums[middle_index] == target:
        return middle_index
    if nums[middle_index] == nums[left_index]:
        return sub_search(nums, middle_index + 1, right_index, target)
    elif nums[middle_index] > nums[left_index]:
        if (nums[left_index] <= target) and (nums[middle_index] > target):
            return sub_search(nums, left_index, middle_index - 1, target)
        else:
            return sub_search(nums, middle_index + 1, right_index, target)
    else:
        if (nums[middle_index] < target) and (nums[right_index] >= target):
            return sub_search(nums, middle_index + 1, right_index, target)
        else:
            return sub_search(nums, left_index, middle_index - 1, target)


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(search(nums, target))
