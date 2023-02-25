# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        highest = 0
        for first in height:
            first_index = 0
            last_index = first_index + 1
            for last in height[height.index(first)+1::]:
                x_asis = last_index - first_index 
                if first >= last:
                    y_asis = last
                else:
                    y_asis = first
                area = x_asis * y_asis
                if area > highest:
                    highest = area
                last_index += 1
            first_index += 1
        return highest
