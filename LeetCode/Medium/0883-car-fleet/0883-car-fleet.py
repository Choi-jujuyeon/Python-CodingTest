class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]

        stack=[]    #target지점까지의 도착하는 시간을 저장

        for p,s in sorted(pair)[::-1]:  #출발지점 내림차순 == 먼거부터 비교하자!
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)