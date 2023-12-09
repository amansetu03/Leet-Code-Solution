from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
def test():
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    print(f"nums = {nums}, target = {target} output = {s.twoSum(nums, target)}")
    nums = [3, 2, 4]
    target = 6
    print(f"nums = {nums}, target = {target} output = {s.twoSum(nums, target)}")
    nums = [3, 3]
    target = 6
    print(f"nums = {nums}, target = {target} output = {s.twoSum(nums, target)}")

print("enter 1 for test and 2 for run")
x = input("")
if x == '1':
    test()
else:
    tc = int(input())
    for _ in range(tc):
        nums = [int(x) for x in input().split()]
        target = int(input())
        S = Solution()
        output = S.twoSum(nums,target)
        print(output)