# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr: #curr not null
            nxt=curr.next        # 다음 노드 저장
            curr.next = prev     # 방향을 틀어!
            prev = curr          # prev를 curr로 이동시킴
            curr = nxt           # 이전에 저장해둔 다음 노드
        return prev
