class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        res = 0
        for i in range(left, right + 1):
            res += self.nums[i]
        return res