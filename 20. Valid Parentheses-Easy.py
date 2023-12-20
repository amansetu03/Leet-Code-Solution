class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or stack.pop() != d[i]:
                    return False
        return not stack
def test(tc):
    s = Solution()
    for i in tc:
        print(f"s = \"{i}\", output = {s.isValid(i)}")
if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = ["()","()[]{}","{]"]
        test(tc)
    else:
        for _ in range(int(input())):
            word = input()
            print(f"s = \"{word}\", output = {s.isValid(word)}")

