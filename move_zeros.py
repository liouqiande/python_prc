# -*- coding: utf-8 -*-
# 283

class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 解法一：遍历列表，将非零元素放入新定义的空列表中，遍历完毕后，将新列表中的元素赋值给原列表，剩下的位置补0
        # 时间复杂度O(n)
        # 空间复杂度O(n)
        # non_zero_element = []
        # for i in range(0, len(nums)):
        #     if nums[i] != 0:
        #         non_zero_element.append(nums[i])
        # for i in range(0, len(non_zero_element)):
        #     nums[i] = non_zero_element[i]
        # for i in range(len(non_zero_element),len(nums)):
        #     nums[i] = 0

        # 解法二：设置指针k，确保[0...k)中的元素都为非0元素
        # 时间复杂度O(n)
        # 空间复杂度O(1)
        # k = 0
        # for i in range(0, len(nums)):
        #     if nums[i] != 0:
        #         nums[k] = nums[i]
        #         k += 1
        # for i in range(k, len(nums)):
        #     nums[i] = 0

        # 解法三：设置指针k，确保[0...k)中的元素都为非0元素
        # 时间复杂度O(n)
        # 空间复杂度O(1)
        k = 0
        for i in range(0, len(nums)):
            if nums[i]:
                # 当列表中有非零元素时，交换两个元素的位置
                if i != k:
                    nums[k], nums[i] = nums[i], nums[k]
                    k += 1
                else:
                    k += 1


if __name__ == "__main__":
    nums = [1,2,3,4,0,5,6]
    sol = Solution()
    sol.moveZeroes(nums)
    print(nums)