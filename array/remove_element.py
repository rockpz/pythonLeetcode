"""
https://leetcode-cn.com/problems/remove-element
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
"""

from typing import List


def remove_element(nums: List[int], val: int) -> int:
    length = 0
    for i, num in enumerate(nums):
        if val != num:
            if length == 0:
                if i == 0:
                    length = length + 1
                else:
                    nums[length] = num
                    length = length + 1
            else:
                nums[length] = num
                length = length + 1
    return length


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    print(remove_element(nums, val))
