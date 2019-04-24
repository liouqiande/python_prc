# -*- coding: utf-8 -*-
# 27

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                if i != k:
                    nums[k], nums[i] = nums[i], nums[k]
                    k += 1
                else:
                    k += 1
        for i in range(k,len(nums)):
            nums.pop()
        return len(nums)

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    sol = Solution()
    sol.removeElement(nums, val)
    print(nums)