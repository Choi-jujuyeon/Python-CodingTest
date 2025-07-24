class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea =0
        stack=[] #pair(index,height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h: #이전 높이가 현재 높이보다 클동안
                index,height = stack.pop()  #계속pop
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h)) #(시작인덱스,높이) pair쌍으로 넣어줌
        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights)-i)) #끝까지 높이가 작았음
        return maxArea

