# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 연결 리스트를 숫자로 바꿔주는 함수
        def l_to_n(list_node):
            s = ""
            while list_node:
                s += str(list_node.val)
                list_node = list_node.next
            return int(s[::-1])
        
        # 숫자를 (거꾸로 된) 연결 리스트로 바꿔주는 함수
        def n_to_l(num):
            # 숫자를 문자열화하여 순서를 거꾸로 바꾼 후 이를 다시 숫자로 바꿔 리스트화해줌
            n_reverse = list(map(int, str(num)[::-1]))
            list_node = ListNode() # 리턴할 연결 리스트 초기화 (첫 번째 노드)
            now = list_node # list_node는 그대로 두고 뒤로 next들을 추가해줄 것이기 때문에 현재 노드를 가리키는 변수(가변하는) 따로 필요
            # 첫 번째 노드는 디폴트 상태(val = 0)로 두고 해당 노드 뒤로 숫자들 연결해주기
            for n in n_reverse:
                now.next = ListNode(val = n) # 새로운 리스트 노드 생성해주되, 생성시 val에 바로 n 대입
                now = now.next # n_reverse의 모든 원소를 다 iterate 한 후에는 마지막 원소의 next가 None인 상태로 종료
            return list_node.next
            
        return n_to_l(l_to_n(l1) + l_to_n(l2))