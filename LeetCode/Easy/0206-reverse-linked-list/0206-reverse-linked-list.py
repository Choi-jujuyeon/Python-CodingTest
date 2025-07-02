# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #sol_1.
        # curr, prev = head, None

        # while curr: #curr not null
        #     nxt=curr.next        # 다음 노드 저장
        #     curr.next = prev     # 방향을 틀어!
        #     prev = curr          # prev를 curr로 이동시킴
        #     curr = nxt           # 이전에 저장해둔 다음 노드
        # return prev
        #------------------------------------------------------

        #sol_2.재귀 활용(단일연결리스트)
        if not head:            #(== if head.next is None:)
            return None         #리스트가 비어있다면, None

        newHead = head          #현재 노드 초기화   
        if head.next:           
            newHead = self.reverseList(head.next)   #재귀 먼저 ㄱㄱ
            head.next.next = head       #방향 반대로 연결
        head.next = None                #원래방향 노드 연결 끊기
        return newHead          
