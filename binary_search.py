# -*- coding: utf-8 -*-
from random import randint


# 在列表arr中查找target元素
def binary_search(arr, target):
    # 在[l...r]的范围里寻找target
    left = 0
    right = int(len(arr)-1)
    while(left <= right):
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            # target 所在区间为[mid+1...r]
            left = mid + 1
        else:
            # target 所在区间为[l...mid-1]
            right = mid - 1
    return -1


def test_binary_search():
    for i in range(100):
        arr = [randint(-10,50) for i in range(20)]
        arr.sort()
        print(arr)
        target = 21
        if binary_search(arr, target) != -1:
            print(str(target) + " in arr")
        else:
            print(str(target) + " not in arr")