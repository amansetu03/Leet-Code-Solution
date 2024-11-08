# '''
# Given an integer array nums, find the minimum and maximum values that can be calculated by summing all element except current element. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#
# Example 1:
# Input: n = 5,  nums = [1,3,5,7,9]
# Output: 16 24
# The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3+5+7+9 = 24 .
#
# Example 2:
# Input: n = 5,  nums = [1,2,3,4,5]
# Output: 10 14
# The numbers are 1,2,3,4,5 and . Calculate the following sums using four of the five integers:
#
# Sum everything except 1, the sum is 2+3+4+5 = 14 .
# Sum everything except 2 , the sum is 1 + 3+4+5 = 13 .
# Sum everything except 3, the sum is 1+2+4+5= 12.
# Sum everything except 4, the sum is 1+2+3+5=11 .
# Sum everything except 5, the sum is 1+2+3+4=10.'''
#
# def find_min_max(arr):
#     # s = 0
#     # for i in arr:
#     #     s += i
#     s = sum(arr)
#     mine = maxe = s-arr[0]#, s - arr[0]
#     for i in range(1,len(arr)):
#         # c = s-arr[i]
#         # if c > maxe:
#         #     maxe = c
#         # elif c<mine:
#         #     mine = c
#         mine = min(mine,s - arr[i])
#         maxe = max(maxe, s - arr[i])
#     return [mine,maxe]
#
#
# if __name__ == "__main__":
#     arr = [int(s) for s in input().split()]
#     print(find_min_max(arr))

def print_petern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or (n-i-1) == j:
                print("*",end="")
            elif (i-j) == 0 and i>(n//2):
                print("*",end="")
            else:
                print(" ",end="")
        print()
    for i in range(n-2):
        for _ in range(n):
                print(" ",end="")
        for j in range(n-2):
            if i==j :
                print("*",end="")
            else:
                print(" ",end="")
        print("")
    for _ in range(n+(n-2)):
            print(" ",end="")
    print("***")

l = int(input("Enter the length: "))
print_petern(l)
