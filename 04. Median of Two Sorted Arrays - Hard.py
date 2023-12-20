from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1+nums2
        arr.sort()
        n = len(arr)
        if n%2 == 1:
            return float(arr[n//2])
        else:
            return float((arr[n//2 -1]+arr[n//2])/2.0)


def test(arr):
    s = Solution()
    for i in arr:
        num1 = i[0]
        num2 = i[1]
        print(f"num1 = '{num1}', num2 = {num2}, your output = {s.findMedianSortedArrays(num1,num2)}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [[[1,3],[2]],[[1,2],[3,4]]]
        test(arr)
    else:
        S = Solution()
        for _ in range(int(input())):
            nums1 = [int(x) for x in input().split()]
            nums2 = [int(x) for x in input().split()]
            output = S.findMedianSortedArrays(nums1,nums2)
            print(output)