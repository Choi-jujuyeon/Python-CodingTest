# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()     
        tail = dummy        
        while l1 and l2 : # not none => 그래야 비교할 수 있음
            if l1.val < l2.val:
                tail.next=l1        # 작은거부터 tail에 연결
                l1= l1.next         # l1 연결 후 업데이트
            else:
                tail.next = l2      
                l2 = l2.next        # l2 연결 후 업데이트 
            tail = tail.next        # tail 포인터는 상관없이 항상 업데이
        # 둘 중 하나의 길이가 남이 있다면?
        if l1:                      
            tail.next=l1
        elif l2:

            tail.next = l2
        return dummy.next

        