"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly
    to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
    This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
"""

class PivotIndexClass:
    def __init__(self):
        pass

    def pivotIndex(self, nums):
        sumLeft = []
        sumRight = []
        sumLeft.append(0)
        sumRight.append(0)
        j = len(nums)
        for i in range(0, len(nums)):
            sumLeft.insert(i + 1, sumLeft[i] + nums[i])
            sumRight.insert(i + 1, sumRight[i] + nums[j - 1 - i])
        print("\nLEFT: ", sumLeft)
        sumRight.reverse()
        print("RIGHT: ", sumRight)
        for i in range(len(sumLeft) - 1):
            if sumLeft[i] == sumRight[i + 1]:
                return i
        return -1
