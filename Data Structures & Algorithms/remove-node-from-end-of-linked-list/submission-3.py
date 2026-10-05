# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        list_len = 0
        curr = head
        
        while curr:
            list_len += 1
            curr = curr.next

        target = list_len - n
        i = 0

        prev = None
        curr = head

        if list_len == 1: return None
        if list_len == n: return head.next

        while curr:
            if i == target:
                print(prev.val, curr.val)
                if curr.next:
                    prev.next = curr.next
                else:
                    prev.next = None
                break
                
            else:
                i += 1
                prev = curr
                curr = curr.next
        
        return head
