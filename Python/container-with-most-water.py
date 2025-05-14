# Time:  O(n)
# Space: O(1)

'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1


Constraints:
    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4


'''


class Solution(object):
    # @return an integer
    def maxArea(self, height):
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area





class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1  #the 2 vertical lines that form the container
        #input l at index 0
        #input r at the ast inde of height array

        mh = max(height)

        res = 0 #initialize result
        while l < r:   #while l pointer < r
            if (r-l) * mh < res:  # if pointers meet or cross, all container have been evaluated
                break
            res = max(res, (r-l)*min(height[l], height[r])) 
            # res = curr width * minimum height of two lines
            if height[l] < height[r]:   #if l is shorter, move l right
                l += 1
            else: #move r left
                r -= 1

        return res  #res = max area found
        