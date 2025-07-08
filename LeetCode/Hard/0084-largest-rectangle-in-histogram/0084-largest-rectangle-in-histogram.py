class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack=[]    #pair: (index,height)

        for i,h in enumerate(heights):          #i:막대의 위치, h:막대의 인덱스
            start = i                           #일단 지금 막대는 자기 위치부터 시작한다고 생각
            
            while stack and stack[-1][1] >h:    #전에 본 막대가 지금보다 더 높으면?
                                                #예전의 높은 막대들은 이제 더 못 커!그러니까 넓이를 계산
                index,height = stack.pop()      # 전에 쌓았던 높은 막대 꺼내기
                maxArea = max(maxArea, height * (i - index))  # 넓이 계산!
                start= index                
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea

