# date: Nov. 21, 2022
# LeetCode Q2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = str()
        result = 0
        
        for char in s:
            if char not in substring:
                substring += char
                result = max(result, len(substring))
            else:
                substring = substring[substring.index(char)+1:] + char
                
        return result
        