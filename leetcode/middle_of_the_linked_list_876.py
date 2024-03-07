# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
	if head is None or head.next is None:
		return head 
	f, s = head, head
	while f and f.next:
		f, s = f.next.next, s.next
	return s
