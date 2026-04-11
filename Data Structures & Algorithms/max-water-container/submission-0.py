class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        area = -1
        while left<right:
            tmp = (right-left)*(min(heights[left],heights[right]))
            area = max(area,tmp)

            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1


        return area

        