from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        ans = ['0'] * n
        for i in range(n):
            ans[indices[i]] = s[i]
        return ''.join(ans)

def test(tc):
    s = Solution()
    for i in tc:
        print(f"s = \"{i[0]}\", indices = {i[1]}, output = \"{s.restoreString(i[0], i[1])}\"")

if __name__ == "__main__":
    n = input("enter 1 for pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [["codeleet",[4,5,6,7,0,2,1,3]],["abc",[0,1,2]]]
        test(tc)
    else:
        for _ in range(int(input())):
            st = input()
            indices = [int(x) for x in input().split()]
            print(f"s = \"{st}\", indices = {indices}, output = \"{s.restoreString(st, indices)}")