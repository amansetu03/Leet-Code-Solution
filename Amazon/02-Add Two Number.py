"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Topic - Linked List, Math, Recursion
"""

from typing import Optional
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print("start...")
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            num_sum = x+y+carry
            carry = num_sum // 10
            curr.next = ListNode(num_sum % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        print("end...")
        return dummy.next


    def insertNode(self, root, item):
        if root is None:
            root= ListNode(item)
        else:
            h = root
            while h.next != None:
                h = h.next
            h.next = ListNode(item)
        return root

    def arrayToList(self, arr):
        root = None
        for i in range(0, len(arr)):
            root = self.insertNode(root, arr[i])

        return root
    def display(self, root):
        h = root
        if h is None:
            print("None")
        while h:
            print(h.val, end=" --> ")
            h = h.next
        print("None")
if __name__ == "__main__":
    t = int(input("enter number of test: "))
    for _ in range(t):
        l1arr = [int(x) for x in input().split()]
        l2arr = [int(s) for s in input().split()]
        s = Solution()
        l1,l2 = s.arrayToList(l1arr), s.arrayToList(l2arr)
        s.display(l1)
        s.display(l2)
        out = s.addTwoNumbers(l1, l2)
        s.display(out)