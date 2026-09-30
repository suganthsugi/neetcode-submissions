class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = []
        currMax = height[0]
        for x in height:
            currMax = max(x, currMax)
            leftMax.append(currMax)
            rightMax.append(0)
        currMax = height[-1]
        for i in range(len(height)-1, -1, -1):
            currMax = max(height[i], currMax)
            rightMax[i] = currMax
        area=0
        for i, x in enumerate(height):
            currMax = min(leftMax[i], rightMax[i])-x
            area+=max(0, currMax)
        return area