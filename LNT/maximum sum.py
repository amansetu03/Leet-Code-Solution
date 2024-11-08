def find_max(arr):
    ans = float("-inf")
    cs = 0
    if len(arr) == 0:
        return 0
    for i in arr:
        if cs<0:
            cs = 0
        cs += i
        ans = max(ans,cs)
    return ans
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = [int(s) for s in input().split()]
        ans = find_max(arr)
        print(ans)