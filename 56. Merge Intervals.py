from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # ans = []
        # size = len(intervals)
        # if size == 1:
        #     return intervals
        # i = 0
        # while i + 1 < size:
        #     if intervals[i][1] >= intervals[i + 1][0]:
        #         ans.append([min(intervals[i][0], intervals[i + 1][0]), max(intervals[i + 1][1], intervals[i][1])])
        #         i += 2
        #     else:
        #         ans.append(intervals[i])
        #         i += 1
        #     print(i)
        # if i == size - 1:
        #     ans.append(intervals[i])
        # return ans
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
def test(arr):
    s = Solution()
    for i in arr:
        print(f"Intervals = {i}")
        print(f"Output = {s.merge(i)}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [[[1,3],[2,6],[8,10],[15,18]],[[1,4],[4,5]]]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            x = int(input("enter number of row "))
            matrix = [0]*x
            for _ in range(x):
                matrix[_] = [int(i) for i in input().split()]
            print(f"Intervals = {matrix}")
            Sol.merge(matrix)
            print(f"Output = {matrix}")