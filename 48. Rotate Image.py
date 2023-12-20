from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
def test(arr):
    s = Solution()
    for i in arr:
        print(f"matrix = {i}")
        s.rotate(i)
        print(f"Output = {i}")
if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [[[1,2,3],[4,5,6],[7,8,9]],[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            x = int(input("enter number of row "))
            matrix = [0]*x
            for _ in range(x):
                matrix[_] = [int(i) for i in input().split()]
            print(f"matrix = {matrix}")
            Sol.rotate(matrix)
            print(f"Output = {matrix}")

