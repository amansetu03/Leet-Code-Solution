from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1


def test(tc):
    s = Solution()
    for i in tc:
        print(f"nums1 = {i[0]},m = {i[1]}, nums2 = {i[2]}, n = {i[3]}")
        s.merge(i[0], i[1], i[2], i[3])
        print(f"output = {i[0]}")

if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [
            [[1,2,3,0,0,0],3,[2,5,6],3],
            [[1],1,[],0],
            [[0],0,[1],1]
        ]
        test(tc)
    else:
        for _ in range(int(input())):
            num1 = [int(x) for x in input().split()]
            m = int(input())
            num2 = [int(x) for x in input().split()]
            n = int(input())
            print(f"nums1 = {num1},m = {m}, nums2 = {num2}, n = {n}")
            s.merge(num1, m, num2, n)
            print(f"output = {num1}")
