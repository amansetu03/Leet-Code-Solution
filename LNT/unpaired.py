def findunp(arr):
    s = arr[0]
    for i in range(1,len(arr)):
        s ^= arr[i]
    print(s)

# use binary search
def binary_find(arr):
    l = 0
    r = len(arr)-1
    while l<r:
        mid = (l + r)//2
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid-1]:
            return arr[mid]


if __name__ == "__main__":
    # t = int(input())
    # for _ in range(t):
    #     arr = [int(s) for s in input().split()]
    #     findunp(arr)

    def search(s):
        l = 0
        r = len(s)-1
        san = ""

        while l<r:
            if s[l] == s[r]:
                san += s[l]
                l = r+1
                r = len(s)-1
            else:
                r -= 1
        print(san)


    # search("qczcquy")
    # search("yy")


def elefent(n):
    if n%5==0:
        print(n//5)
    else:
        print((n//5)+1)


